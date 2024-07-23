import requests
import csv
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# URL base para a API
base_url = "https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao"

# Parâmetros iniciais para a consulta
params = {
    "dataInicial": "20230101",
    "dataFinal": "20240101",
    "codigoModalidadeContratacao": "08",
    "tamanhoPagina": 50
}

# Função para obter os dados de uma página específica
def get_page_data(page_number):
    params["pagina"] = page_number
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao acessar a página {page_number}: {response.status_code}")
        return None

# Função para obter o número total de páginas
def get_total_pages():
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['totalPaginas']
    else:
        print(f"Erro ao acessar a página inicial: {response.status_code}")
        return 0

# Lista para armazenar todos os dados
all_data = []

# Obter o número total de páginas
total_pages = get_total_pages()
print(f"Número total de páginas: {total_pages}")

# Obter o número máximo de workers com base no número de CPUs disponíveis
max_workers = os.cpu_count()
print(f"Usando {max_workers} workers")

# Usando ThreadPoolExecutor para paralelizar as solicitações
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    # Criando uma lista de futuros para cada página
    futures = [executor.submit(get_page_data, page_number) for page_number in range(1, total_pages + 1)]

    for future in as_completed(futures):
        data = future.result()
        if data and 'data' in data:
            # Filtrando apenas os registros com amparoLegal.codigo = 24
            filtered_data = [item for item in data['data'] if item.get('amparoLegal', {}).get('codigo') == 24]
            # Modificando o campo amparoLegal para conter apenas a descrição
            for item in filtered_data:
                item['amparoLegal'] = item['amparoLegal']['descricao']
            all_data.extend(filtered_data)

print(f"Total de itens coletados: {len(all_data)}")

# Salvando os dados em um arquivo CSV
csv_file = 'dados_filtrados_todas_paginas.csv'

# Determinando os cabeçalhos a partir das chaves do primeiro item
if all_data:
    keys = all_data[0].keys()

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_data)

    print(f"Dados salvos em {csv_file}")
else:
    print("Nenhum dado encontrado para salvar.")

import requests
import csv
import time

# URL base da API
base_url = "https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao"

# Parâmetros iniciais para a consulta
params = {
    "dataInicial": "20240101",
    "dataFinal": "20240601",
    "codigoModalidadeContratacao": "08",
}

# Função para realizar uma requisição e repetir até obter um resultado válido
def fetch_page(page_number):
    print(f"Iniciando busca para a página {page_number}...")
    # Atualiza o número da página nos parâmetros da requisição
    params["pagina"] = page_number
    while True:
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()  # Verifica se a resposta contém um status de erro HTTP
            data = response.json()
            # Condição de saída: Verifica se há resultados na resposta
            if 'data' in data and data['data']:
                print(f"Dados obtidos com sucesso para a página {page_number}")
                return data
            else:
                print(f"Nenhum resultado na página {page_number}, tentando novamente.")
        except requests.RequestException as e:
            print(f"Erro na página {page_number}, tentando novamente. Erro: {e}")
        time.sleep(2)  # Espera antes de tentar novamente

# Função principal para processar as páginas sequencialmente
def process_pages(total_pages):
    results = []
    print(f"Processando um total de {total_pages} páginas...")
    for page in range(1, total_pages):
        data = fetch_page(page)
        # Filtra os resultados com base no critério especificado
        for item in data.get('resultados', []):
            amparos = item.get('amparoLegal', {})
            if amparos.get('codigo') == 24:
                results.append(item)
        print(f"Página {page} processada.")
    print(f"Processamento de todas as páginas concluído.")
    return results

# Função para salvar os resultados em um arquivo CSV
def save_to_csv(results, filename):
    print(f"Salvando resultados no arquivo {filename}...")
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escreve o cabeçalho
        writer.writerow([
            "modalidadeId", "srp", "anoCompra", "sequencialCompra", "orgaoSubRogado",
            "orgaoEntidade_cnpj", "orgaoEntidade_razaoSocial", "orgaoEntidade_poderId", "orgaoEntidade_esferaId",
            "dataInclusao", "dataPublicacaoPncp", "dataAtualizacao", "numeroCompra",
            "unidadeOrgao_ufNome", "unidadeOrgao_codigoUnidade", "unidadeOrgao_nomeUnidade",
            "unidadeOrgao_ufSigla", "unidadeOrgao_municipioNome", "unidadeOrgao_codigoIbge",
            "amparoLegal_codigo", "amparoLegal_descricao", "amparoLegal_nome", "dataAberturaProposta",
            "dataEncerramentoProposta", "informacaoComplementar", "processo", "objetoCompra",
            "linkSistemaOrigem", "justificativaPresencial", "unidadeSubRogada", "valorTotalHomologado",
            "modoDisputaId", "numeroControlePNCP", "valorTotalEstimado", "modalidadeNome", "modoDisputaNome",
            "tipoInstrumentoConvocatorioCodigo", "tipoInstrumentoConvocatorioNome", "situacaoCompraId",
            "situacaoCompraNome", "usuarioNome"
        ])
        # Escreve os dados
        for result in results:
            print("resultado salvo")
            writer.writerow([
                result.get("modalidadeId"),
                result.get("srp"),
                result.get("anoCompra"),
                result.get("sequencialCompra"),
                result.get("orgaoSubRogado"),
                result.get("orgaoEntidade", {}).get("cnpj"),
                result.get("orgaoEntidade", {}).get("razaoSocial"),
                result.get("orgaoEntidade", {}).get("poderId"),
                result.get("orgaoEntidade", {}).get("esferaId"),
                result.get("dataInclusao"),
                result.get("dataPublicacaoPncp"),
                result.get("dataAtualizacao"),
                result.get("numeroCompra"),
                result.get("unidadeOrgao", {}).get("ufNome"),
                result.get("unidadeOrgao", {}).get("codigoUnidade"),
                result.get("unidadeOrgao", {}).get("nomeUnidade"),
                result.get("unidadeOrgao", {}).get("ufSigla"),
                result.get("unidadeOrgao", {}).get("municipioNome"),
                result.get("unidadeOrgao", {}).get("codigoIbge"),
                result.get("amparoLegal", {}).get("codigo"),
                result.get("amparoLegal", {}).get("descricao"),
                result.get("amparoLegal", {}).get("nome"),
                result.get("dataAberturaProposta"),
                result.get("dataEncerramentoProposta"),
                result.get("informacaoComplementar"),
                result.get("processo"),
                result.get("objetoCompra"),
                result.get("linkSistemaOrigem"),
                result.get("justificativaPresencial"),
                result.get("unidadeSubRogada"),
                result.get("valorTotalHomologado"),
                result.get("modoDisputaId"),
                result.get("numeroControlePNCP"),
                result.get("valorTotalEstimado"),
                result.get("modalidadeNome"),
                result.get("modoDisputaNome"),
                result.get("tipoInstrumentoConvocatorioCodigo"),
                result.get("tipoInstrumentoConvocatorioNome"),
                result.get("situacaoCompraId"),
                result.get("situacaoCompraNome"),
                result.get("usuarioNome")
            ])
    print(f"Resultados salvos com sucesso no arquivo {filename}.")

# Número total de páginas a serem consultadas
total_pages = 23442  # Ajuste conforme necessário

print("Iniciando o processo de consulta de dados...")
# Executa o processamento das páginas
results = process_pages(total_pages)

# Salva os resultados em um arquivo CSV
save_to_csv(results, 'resultados_filtrados.csv')

print(f"Processamento concluído. {len(results)} registros salvos em 'resultados_filtrados.csv'.")

import requests
import csv
from datetime import datetime, timedelta

campos = [
    'codigo_do_item_no_catalogo',
    'data_abertura_proposta',
    'data_entrega_edital',
    'data_entrega_proposta',
    'data_publicacao',
    'endereco_entrega_edital',
    'funcao_responsavel',
    'identificador',
    'informacoes_gerais',
    'modalidade',
    'nome_responsavel',
    'numero_aviso',
    'numero_item_licitacao',
    'numero_itens',
    'numero_processo',
    'objeto',
    'situacao_aviso',
    'tipo_pregao',
    'tipo_recurso',
    'uasg'
]

# Função para buscar dados da API e salvar em um arquivo CSV
def buscar_e_salvar_csv(data_inicio, data_fim, arquivo_saida):
    url_base = "http://compras.dados.gov.br/compraSemLicitacao/v1/compras_slicitacao.json?dt_publicacao="
    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
            'co_orgao', 'co_orgao_superior', 'co_uasg', 'co_modalidade_licitacao',
            'ds_lei', 'nu_inciso', 'nu_processo', 'qt_total_item', 'vr_estimado',
            'nu_aviso_licitacao', 'ds_objeto_licitacao', 'ds_fundamento_legal',
            'ds_justificativa', 'dtDeclaracaoDispensa', 'no_responsavel_decl_disp',
            'no_cargo_resp_decl_disp', 'dtRatificacao', 'no_responsavel_ratificacao',
            'no_cargo_resp_ratificacao', 'dtPublicacao', '_links'
        ])
        writer.writeheader()

        # Loop através das datas
        data_atual = data_inicio
        while data_atual <= data_fim:
            data_str = data_atual.strftime("%Y%m%d")
            url = url_base + data_str
            response = requests.get(url)
            if response.status_code == 200:
                dados = response.json()
                print(dados)
                compras = dados['_embedded']['compras']
                if compras:
                    for compra in compras:
                        writer.writerow(compra)
            # Incrementar data
            data_atual += timedelta(days=1)

# Definir datas de início e fim
data_inicio = datetime(2023, 1, 1)
data_fim = datetime(2023, 12, 31)

# Nome do arquivo de saída
arquivo_saida = "request_anos.csv"

# Chamar a função para buscar e salvar os dados em um arquivo CSV
buscar_e_salvar_csv(data_inicio, data_fim, arquivo_saida)
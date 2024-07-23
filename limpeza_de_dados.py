import pandas as pd
from collections import Counter

# Caminho para o arquivo CSV
caminho_arquivo = "dados/request_anos.csv"

# Colunas que você deseja manter
colunas_desejadas = ["co_modalidade_licitacao", "vr_estimado", "ds_objeto_licitacao", "ds_fundamento_legal", "ds_justificativa"]

# Ler o arquivo CSV mantendo apenas as colunas desejadas
dados = pd.read_csv(caminho_arquivo, usecols=colunas_desejadas, encoding='utf-8')
palavras_remover = ['Justificativa: ', 'Lei', 'Art.', 'nº ']

# Use a função replace() para remover todas as ocorrências das palavras da lista
for palavra in palavras_remover:
    dados['ds_justificativa'] = dados['ds_justificativa'].str.replace(palavra, '')

# Salvar os dados em um novo arquivo CSV, se desejar
dados.to_csv("dados/request_anos_utf8.csv", index=False, encoding='utf-8')
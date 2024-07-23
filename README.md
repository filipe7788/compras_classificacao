
# README

---

## Introdução

Este repositório contém scripts Python que realizam a coleta, limpeza, classificação e análise de dados de compras públicas. A seguir, detalhamos o propósito de cada arquivo, como instalar as dependências e como visualizar os resultados.

## Estrutura do Repositório

### `classification.py`
Este script é responsável por:
- Carregar dados de compras públicas a partir de um arquivo CSV.
- Pré-processar o texto das justificativas, removendo palavras irrelevantes (stop words) e tokenizando o texto.
- Extrair características textuais usando o método TF-IDF (Term Frequency-Inverse Document Frequency).
- Realizar agrupamento (clustering) dos textos usando o algoritmo KMeans.
- Gerar nuvens de palavras (word clouds) para visualizar os termos mais frequentes em cada cluster.

O código utiliza bibliotecas como `nltk` para processamento de texto, `sklearn` para clustering e `wordcloud` para visualização, conforme pode ser visto nas linhas que importam essas bibliotecas e implementam esses passos.

### `coleta_compras.py`
Este script é responsável por:
- Realizar requisições a uma API para coletar dados de compras públicas.
- Processar os resultados das requisições e extrair campos específicos.
- Salvar os dados coletados em arquivos CSV.
### `coleta_de_dados.py`
Este script auxilia na coleta de dados, fornecendo funções e métodos complementares usados em `coleta_compras.py`.

### `limpeza_de_dados.py`
Este script é responsável por:
- Limpar e preparar os dados coletados para análise posterior.
- Remover ou corrigir dados inconsistentes ou inválidos.
  
### `pegar_novos_dados.py`
Este script é responsável por:
- Buscar novos dados de compras públicas que ainda não foram coletados.
- Atualizar os arquivos existentes com os novos dados.

## Instalação

### Requisitos

Certifique-se de ter o Python 3.6+ instalado. Recomenda-se o uso de um ambiente virtual para evitar conflitos de dependências.

### Passos de Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/filipe7788/compras_classificacao
    cd compras_classificacao
    ```

2. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scriptsctivate`
    ```

3. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

### Coleta de Dados

Para coletar dados de compras públicas, execute:

```bash
python coleta_compras.py
```

Este script coletará os dados e salvará em arquivos CSV no diretório `dados`.

### Limpeza de Dados

Para limpar e preparar os dados para análise, execute:

```bash
python limpeza_de_dados.py
```

Este script processará os dados coletados e gerará um arquivo CSV limpo e pronto para análise.

### Classificação de Dados

Para classificar os dados de compras públicas, execute:

```bash
python classification.py
```

Este script realizará a classificação dos dados e salvará os resultados em um arquivo CSV.

### Buscar Novos Dados

Para buscar novos dados de compras públicas, execute:

```bash
python pegar_novos_dados.py
```

Este script buscará novos dados e atualizará os arquivos existentes.

## Visualização dos Resultados

Os resultados da coleta, limpeza e classificação de dados são salvos em arquivos CSV no diretório `dados`. Você pode visualizar esses arquivos usando qualquer editor de planilhas, como Microsoft Excel, Google Sheets ou softwares especializados em análise de dados como pandas no Python.

### Exemplo de Visualização com Pandas

Aqui está um exemplo de como carregar e visualizar os dados usando pandas no Python:

```python
import pandas as pd

# Carregar os dados processados
df = pd.read_csv('dados/dados_processados_utf8.csv')

# Exibir as primeiras linhas do DataFrame
print(df.head())
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.


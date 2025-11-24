# ETL – Coleta e Processamento de Dados de Jogos da Steam

Este projeto realiza um processo completo de **ETL (Extract, Transform, Load)** para coletar informações da Steam Store API e Steam Reviews API, tratar os dados recebidos e armazená-los em um arquivo CSV utilizando **Pandas**.

A pipeline foi estruturada em três etapas principais: **extração**, **transformação** e **carga**.

---

## Objetivo do Projeto

Automatizar a coleta de informações de jogos da Steam a partir de uma lista de IDs (AppIDs), tratar e padronizar os dados retornados pelas APIs oficiais e consolidar tudo em um DataFrame salvo no formato **CSV**.

---

## Arquitetura da Pipeline

app/
 └── pipelines/
      ├── extrair.py
      ├── transformar.py
      └── carregar.py
main.py

data/
 ├── input/
 │     steamcmd_appid.csv
 └── output/
       API_STEAM_GAMES_TODOS.csv


---

## Etapas do ETL

### 1. Extração – `extraindo_dados_API`

- Utiliza os endpoints da Steam:
  - `https://store.steampowered.com/api/appdetails`
  - `https://store.steampowered.com/appreviews`
- Coleta informações como:
  - Tipo e nome do jogo  
  - Descrição curta  
  - Desenvolvedores e publishers  
  - Plataformas suportadas  
  - Gênero  
  - Data de lançamento  
  - Preço  
  - Avaliações (positivas, negativas, totais)

Somente jogos com retorno bem-sucedido são processados.

---

### 2. Transformação – `transformacao_dados`

- Limpa e padroniza campos retornados pela API.
- `supported_languages` é convertido para uma lista:
  - Remove HTML com **BeautifulSoup**
  - Remove marcadores de aúdio
- `platforms` é convertido para uma lista com somente plataformas suportadas.

---

### 3. Carga – `carregar_dados_csv`

- Garante a existência da pasta de saída.
- Converte listas e dicionários para strings antes da exportação.
- Cria um DataFrame consolidado com todos os jogos.
- Exporta em CSV.

---

## Execução – `main.py`

O script principal realiza:

1. Leitura do CSV com AppIDs (`steamcmd_appid.csv`)
2. Filtro inicial a partir de um ID específico (`ID_INICIAL`)
3. Processamento sequencial até atingir `NUM_JOGOS_VALIDOS`
4. Logs de tentativa por ID
5. Extração → transformação → armazenamento
6. Geração final do CSV em `data/output`

---

##  Dependências

- Python 3.x  
- requests  
- pandas  
- beautifulsoup4  

Instalação:

```bash
pip install -r requirements.txt


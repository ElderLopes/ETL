# Desafio ETL com Python

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-green.svg)](https://pandas.pydata.org/)

## 📖 Sobre o Projeto
O objetivo principal é demonstrar o domínio sobre o fluxo **ETL (Extract, Transform, Load)** utilizando a linguagem Python.


## ⚙️ Funcionalidades Implementadas
O pipeline de dados executa os seguintes passos:
1. **Extração (E):** Lê os dados de clientes (ID, Nome, Conta, Cartão) de um arquivo `usuarios.csv` utilizando a biblioteca Pandas.
2. **Transformação (T):** Processa os dados extraídos e cria uma nova coluna, gerando uma mensagem de marketing personalizada para cada cliente (simulando uma inteligência de recomendação).
3. **Carregamento (L):** Exporta a base de dados enriquecida para um novo arquivo chamado `usuarios_transformados.csv`, preservando os dados originais.

## 📂 Estrutura do Projeto
```text
📦 ETL
 ┣ 📜 usuarios.csv                 # Banco de dados original (Entrada)
 ┣ 📜 usuarios_transformados.csv   # Banco de dados enriquecido (Saída)
 ┣ 📜 etl.py                       # Script principal contendo o pipeline ETL
 ┗ 📜 README.md                    # Documentação do projeto
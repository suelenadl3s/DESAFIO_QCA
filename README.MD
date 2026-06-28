# Automação de Processamento de Faturas

## Sobre o projeto

Este projeto foi desenvolvido por Suelen Ádles como parte de um desafio técnico de estágio da QCA.

A aplicação realiza a leitura de arquivos PDF contendo faturas, extrai as informações necessárias, valida os dados e organiza tudo em um formato estruturado para análise. Após o processamento, os dados são armazenados em um arquivo JSON local e utilizados para gerar análises com Pandas.

A estrutura foi organizada separando responsabilidades para facilitar manutenção e entendimento do fluxo.

## Fluxo do sistema

PDF → Extração (pdfplumber) → Validação (Pydantic) → Persistência (JSON) → Análise (Pandas)

## Decisões de arquitetura

O projeto foi dividido em camadas para manter o código organizado e facilitar futuras alterações.

A camada ingestion é responsável pela leitura e extração dos dados dos PDFs.  
A camada schemas é responsável pela validação e estruturação dos dados utilizando Pydantic.  
A camada models define as entidades utilizadas no sistema.  
A camada analytics é responsável pelas análises e agregações com Pandas.  
O arquivo database.json é utilizado como persistência local dos dados processados.

A separação foi feita para evitar acoplamento entre leitura, validação e análise.

## Funcionalidades

- Leitura de múltiplos arquivos PDF
- Extração de dados das faturas: Order ID, Data, Customer ID, Produtos, Quantidade e Preço unitário
- Validação dos dados com Pydantic
- Persistência dos dados em JSON local
- Controle de duplicidade via Order ID
- Análises com Pandas:
  - Média do valor das faturas
  - Produto mais comprado
  - Total gasto por produto
  - Lista de produtos com valores unitários

## Estrutura do projeto

.
├── analytics/
├── data/
│   └── pdfs/
├── database.json
├── ingestion/
├── models/
├── schemas/
├── src/
├── main.py
├── requirements.txt
└── README.md

## Tecnologias utilizadas

Python 3.13  
pdfplumber  
Pydantic  
Pandas  

## Como executar o projeto

Clone o repositório:

git clone <url-do-repositorio>

Acesse a pasta:

cd DESAFIO_QCA

Crie um ambiente virtual:

python -m venv venv

Ative o ambiente:

Windows:
venv\Scripts\activate

Linux/macOS:
source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

## Execução

Coloque os arquivos PDF na pasta data/pdfs/

Execute o projeto:

python main.py

## Resultado

Ao final da execução, o sistema gera um arquivo database.json contendo os dados processados e exibe análises com base nesses registros.

As análises incluem média do valor das faturas, produto mais frequente, total gasto por produto e listagem de produtos com seus valores unitários.

## Observação

O projeto foi desenvolvido com foco em organização, clareza e separação de responsabilidades, seguindo uma estrutura em camadas para facilitar manutenção e evolução.
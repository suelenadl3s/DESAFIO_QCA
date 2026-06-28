# Automação de Processamento de Faturas

## Sobre o projeto

Esse projeto foi desenvolvido por Suelen Ádles como parte de um desafio técnico de estágio da QCA.

A ideia é ler arquivos PDF de faturas, extrair as informações necessárias, validar os dados e salvar tudo em um JSON local. Depois disso, são feitas algumas análises usando Pandas.

O projeto foi separado em módulos para facilitar organização e manutenção.

## O que ele faz

- Lê arquivos PDF de uma pasta
- Extrai informações das faturas: Order ID, Data, Customer ID, Produtos, Quantidade e Preço unitário
- Valida os dados com Pydantic
- Salva os dados em um arquivo JSON
- Evita duplicidade usando Order ID
- Faz análises com Pandas, como média do valor das faturas, produto mais comprado, total gasto por produto e lista de produtos com valores

## Estrutura do projeto

.
├── analytics/
├── data/
│   └── pdfs/
├── database/
├── ingestion/
├── models/
├── schemas/
├── main.py
├── requirements.txt
└── README.md

## Tecnologias usadas

Python 3.13  
pdfplumber  
Pydantic  
Pandas  

## Base utilizada no desenvolvimento

Durante o desenvolvimento foram utilizadas documentações oficiais e referências para garantir boas práticas e organização do código:

Python Documentation: https://docs.python.org/3/  
pdfplumber: https://github.com/jsvine/pdfplumber  
Pydantic: https://docs.pydantic.dev/  
Pandas: https://pandas.pydata.org/docs/  
PEP 8: https://peps.python.org/pep-0008/

## Como rodar

Clone o repositório:
git clone <url-do-repositorio>

Entre na pasta:
cd <nome-do-projeto>

Crie o ambiente virtual:
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

Ao final da execução o sistema exibe:

- Média das faturas
- Produto mais comprado
- Total gasto por produto
- Lista de produtos com valores

Os dados são salvos em database.json.

Se o arquivo não existir ele será criado automaticamente. Se já existir uma fatura com o mesmo Order ID, ela não será duplicada.

## Observação

O projeto foi construído com foco em organização, clareza e separação de responsabilidades entre ingestão, validação e análise de dados, seguindo boas práticas das documentações utilizadas.
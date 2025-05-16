# Eai-Back-end
Desenvolvimento do Back end de um crm de entregas

Criação do ambiente e instalação dos frameworks
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Vamos hospedar no render, para fazer isso, precisamos dos arquivos abaixo:
render.yaml - Configuração para hospedar o render
requirements.txt -> Frameworks e suas versões

Utilizando o .env importamos os seguintes dados:

from dotenv import load_dotenv -> Importar o env colocando o apelido load_dotenv,
load_dotenv() -> iniciando o .env
import os -> Importamos o modulo 'os' para coletar informações dentro do .env
port = int(os.getenv("PORT")) -> como importamos a variavel "PORT" do env como "int"






###
Abra o CMD -> Escreva sqlite3 ou sqlite3 "nome do seu banco sem aspas" para entrar no sqlite3
Para listar todas as tabelas basta digitar .table
Para listar todos comandos basta .help

Nome do database:  database/eai.db

Criar tabela de usuarios no sqlite

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    empresa TEXT NOT NULL
);

Isnsert de dados

INSERT INTO usuarios (nome, email, senha, empresa)
VALUES ('Gabriel Lopes', 'gabriel@eai.com', 'admineai', 'Eai Gestão');
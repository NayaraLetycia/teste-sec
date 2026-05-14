import os

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")

def start_session():
    if not AWS_ACCESS_KEY:
        return "Erro: Chave não configurada!"
    return "Chave configurada com sucesso"
print(start_session())

import sqlite3
#se alguém substitui o valor da variável por 1 or 1=1, essa query pode retornar todos os dados

def busca_usuario(user_id):
    query = "SELECT * FROM usuarios WHERE id = " + user_id
    
    print(f"Executando query: {query}")
    return "Dados do usuário retornados"
busca_usuario("10")

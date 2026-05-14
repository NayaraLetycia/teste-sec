import os

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")

def start_session():
    if not AWS_ACCESS_KEY:
        return "Erro: Chave não configurada!"
    return "Chave configurada com sucesso"
print(start_session())

############################################## 1

import sqlite3
#se alguém substitui o valor da variável por 1 or 1=1, essa query pode retornar todos os dados

def busca_usuario(user_id):
    query = "SELECT * FROM usuarios WHERE id = " + user_id
    
    print(f"Executando query: {query}")
    return "Dados do usuário retornados"
busca_usuario("10")

################################################ 2
import os

def ping_host(hostname):
    # VULNERÁVEL: Se hostname for "google.com ; rm -rf /", o comando deleta tudo
    os.system("ping -c 1 " + hostname)

ping_host("8.8.8.8")

################################################ 3 
#import pickle
import json

def carregar_configuracao(dados_binarios_json):
    # VULNERÁVEL: Pode executar código arbitrário ao carregar. Melhor escolher um JSON, que só transportam dados
    return json.loads(dados_binarios_json)

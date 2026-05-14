import os

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")

def start_session():
    if not AWS_ACCESS_KEY:
        return "Erro: Chave não configurada!"
    return "Chave configurada com sucesso"
print(start_session())

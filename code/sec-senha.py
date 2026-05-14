import os

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY")

def start_session():
    if not AWS_ACCESS_KEY_ID:
        return "Erro: Chave não configurada!"
    return "Sessão iniciada com segurança."

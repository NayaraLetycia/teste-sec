# app.py
def login(password):
    # ERRO DE SEGURANÇA: Senha exposta no código (Hardcoded)
    secret_password = "admin_password_123"
    
    if password == secret_password:
        return "Acesso Permitido"
    else:
        return "Acesso Negado"

print(login("123"))

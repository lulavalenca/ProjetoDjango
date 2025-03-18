import re

def validar_email(email):
    """
    Verifica se um endereço de e-mail é valido.
    
    :param email: String contendo o endereço de e-mail a ser validado.
    :return: True se o e-mail for valido, False caso contrário.
    """
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(regex, email):
        return True
    else:
        return False

# Exemplos de uso
emails = [
    "usuario@exemplo.com",
    "usuario.exemplo.com",
    "usuario@exemplo",
    "usuario@exemplo.",
    "usuario@exemplo..com",
    "usuario@exemplo.c",
    "usuario@exemplo.com.br",
    "usuario+alias@exemplo.com",
    "usuario@exemplo.co.uk",
    
]    

for email in emails:
    print(f"E-mail: {email} -> Valido? {validar_email(email)}")
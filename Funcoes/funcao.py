def somar(a, b):
    resultado = a + b
    return resultado


numero1 = 10
numero2 = 30
total = numero1 + numero2
print("o total da soma de numero1, e numero2 é: ", total)

def envia_email(nome, email):
    nome_dest = nome
    email_dest = email
    return f'Email enviado para {nome_dest}, dona do email {email_dest}'
    
pessos = [
    {   'nome': 'BRUNO', 
        'email': 'bbcoxinha@gmail.com'   
    },
    { 'nome': 'Creuza',
      'email': 'crx@gmail.com' 
    }
]
    
for pessoa in pessos:
    email_enviado = envia_email(pessoa['nome'], pessoa['email'])
    print(email_enviado)
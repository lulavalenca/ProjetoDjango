import api
import os

ambiente = os.getenv('AMBIENTE')
usuario = os.environ.get("USUARIO_API")
senha = os.environ.get('SENHA_API')

print(usuario)
print(senha)


login = api.login(usuario, senha)
print(login)

if ambiente == 'dev':
    print(api.envia_email_log())
    
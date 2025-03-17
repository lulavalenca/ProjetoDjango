
texto = "AULA PYCODEBR"

# Exibir o tamanho da string
print(len(texto))

# Exibir os caracteres a partir do índice 5 até o final
print(texto[5:])

# Exibir os caracteres do índice 5 ao 10 (11 não é incluído)
print(texto[5:11])

#
print(texto.count('A')) 

print(texto.count('E', 5, 11))

print(texto.find("AULA"))

print(texto.upper())

print(texto.lower())

print(texto.capitalize())

print(texto.title())

lista_de_palavras = texto.split()
resultado = '_'.join(lista_de_palavras)
print(resultado)

texto = '    AULA PYCODEBR   '
texto.strip()
print(texto)

texto = '    AULA PYCODEBR   '
texto.rstrip()
print(texto)

texto = '   AULA PYCODEBR   '
texto.lstrip()
print(texto)
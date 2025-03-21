"""
A compreensão de listas (ou list comprehension) 
é uma forma concisa e eficiente de criar listas em Python.
Ela permite que você gere uma nova lista aplicando uma expressão
a cada item de uma sequência (como uma lista, tupla, string, etc.) e,
opcionalmente, 
filtrar elementos com uma condição.

"""

#nova_lista = [expressao for item in iteravel if condicao]


# 1 Criar uma lista de quadrados:
quadrados = [x**2 for x in range(10)]
print(quadrados) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#
numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

#

numeros = [1, 2, 3, 4, 5]

def dobro(numero):
    return numero * 2

numeros_dobrados = [dobro(numero) for numero in numeros]

print(numeros_dobrados)

#Nomes maiusculos 
nomes = ['Luiz', 'Felipe', 'João', 'Monica', 'Bia']

nomes_maiusculos = [nome.upper() for nome in nomes if nome[0] == 'L' and nome[1] == 'M']

print(nomes_maiusculos)

#
nomes = ['Luiz', 'Felipe', 'João', 'Monica', 'Bia']

# Filtra os nomes que começam com 'L' ou 'M' e os transforma em maiúsculas
nomes_filtrados = [nome.upper() for nome in nomes if nome[0] in ['F', 'B']]

# Imprime a lista com os nomes filtrados e em maiúsculas
print(nomes_filtrados)
# Lista de carros
carros = []
carros.append("Santana")
carros.extend(["Gol", "Saveiro"])  # Corrigido para adicionar múltiplos elementos corretamente
print("Lista de carros:", carros)

# Criando listas em Python
lista_vazia = []
numeros = [1, 2, 3, 4, 5]
frutas = ["maçã", "banana", "laranja"]
lista_mista = [10, "Python", 3.14, True]

# Manipulação de listas
frutas.append("uva")
print("Lista de frutas após append:", frutas)

frutas.insert(1, "morango")
print("Lista de frutas após insert:", frutas)

frutas.extend(["abacaxi", "manga"])
print("Lista de frutas após extend:", frutas)

frutas.remove("banana")
print("Lista de frutas após remover banana:", frutas)

ultimo = frutas.pop()
print("Elemento removido com pop:", ultimo)
print("Lista de frutas após pop:", frutas)

posicao = frutas.index("laranja")
print("Posição da laranja na lista:", posicao)

lista_numeros = [1, 2, 2, 3, 4, 2, 5]
quantidade = lista_numeros.count(2)
print("Quantidade de vezes que o 2 aparece:", quantidade)

# Ordenação e cópia de listas
numeros = [5, 1, 8, 3, 2]
numeros.sort()
print("Números ordenados:", numeros)

numeros.reverse()
print("Lista invertida:", numeros)

nova_lista = numeros.copy()
print("Cópia da lista de números:", nova_lista)

# Limpando a lista de frutas
frutas.clear()
print("Lista de frutas após clear:", frutas)

# Exemplo 1: Criar uma lista dinâmica com entrada do usuário
nomes = []
for i in range(3):
    nome = input("Digite um nome: ")
    nomes.append(nome)

print("Lista de nomes:", nomes)

# Exemplo 2: Filtrar números pares de uma lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", pares)

# Exemplo 3: Remover itens duplicados
lista_duplicada = [1, 2, 2, 3, 4, 4, 5]
lista_sem_duplicadas = list(set(lista_duplicada))
print("Lista sem duplicatas:", lista_sem_duplicadas)

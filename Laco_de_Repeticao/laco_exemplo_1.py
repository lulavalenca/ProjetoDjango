# Função que simula o envio de um email para o cliente
def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')

# Lista de clientes
clientes = ['ANA', 'Pedro', 'Felipe', 'Claudio', 'Renato']

# ---------------------------
# Exemplo 1: Acessando o primeiro cliente diretamente
# ---------------------------
# Exibindo o primeiro cliente da lista
print("Exemplo 1: Acessando o primeiro cliente diretamente")
print(clientes[0])  # Acessa diretamente o primeiro cliente

# ---------------------------
# Exemplo 2: Usando enumerate() para obter índice e nome do cliente
# ---------------------------
# A função enumerate() retorna uma tupla com o índice e o valor do item
print("\nExemplo 2: Usando enumerate() para obter índice e nome do cliente")
for cliente in enumerate(clientes):
    print(cliente)  # Exibe o índice e o nome do cliente

# ---------------------------
# Exemplo 3: Enviando email para todos os clientes usando for simples
# ---------------------------
print("\nExemplo 3: Enviando email para todos os clientes usando for simples")
for cliente in clientes:
    envia_email(cliente)  # Envia o email para cada cliente da lista

# ---------------------------
# Exemplo 4: Usando enumerate() e break para parar após o terceiro cliente
# ---------------------------
print("\nExemplo 4: Enviando email para os clientes até o 3º, depois parando (break)")
for i, cliente in enumerate(clientes):
    if i == 2:  # O índice começa em 0, então i == 2 é o terceiro cliente
        break  # Interrompe o loop quando atingir o índice 2
    envia_email(cliente)  # Envia o email para o cliente até o índice 2

# ---------------------------
# Exemplo 5: Usando enumerate() e continue para pular o terceiro cliente
# ---------------------------
print("\nExemplo 5: Enviando email para todos, exceto o 3º (usando continue)")
for i, cliente in enumerate(clientes):
    if i == 2:  # Pula o terceiro cliente (índice 2)
        continue  # Pula esta iteração e vai para a próxima
    envia_email(cliente)  # Envia o email para os outros clientes

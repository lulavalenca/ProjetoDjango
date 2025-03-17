# Função que simula o envio de um email para o cliente
def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')

# Lista de clientes
clientes = ['ANA', 'Pedro', 'Felipe', 'Claudio', 'Renato']

# ---------------------------
# Exemplo 1: Acessando o primeiro cliente diretamente
# ---------------------------
# Acessando diretamente o primeiro cliente
print("Exemplo 1: Acessando o primeiro cliente diretamente com while")
i = 0  # Inicia o índice
while i < 1:  # Condição para o loop
    print(clientes[i])  # Exibe o primeiro cliente
    i += 1  # Incrementa o índice

# ---------------------------
# Exemplo 2: Usando while para iterar e exibir os clientes
# ---------------------------
# Usando while para exibir os clientes de forma sequencial
print("\nExemplo 2: Usando while para iterar e exibir os clientes")
i = 0  # Inicializa o índice
while i < len(clientes):  # O loop vai até o tamanho da lista
    print(clientes[i])  # Exibe o cliente na posição i
    i += 1  # Incrementa o índice para o próximo cliente

# ---------------------------
# Exemplo 3: Enviando email para todos os clientes usando while
# ---------------------------
print("\nExemplo 3: Enviando email para todos os clientes usando while")
i = 0  # Inicializa o índice
while i < len(clientes):  # Vai iterar enquanto o índice for menor que o tamanho da lista
    envia_email(clientes[i])  # Envia o email para o cliente atual
    i += 1  # Incrementa o índice para o próximo cliente

# ---------------------------
# Exemplo 4: Usando while e break para parar após o terceiro cliente
# ---------------------------
print("\nExemplo 4: Enviando email para os clientes até o 3º, depois parando (break)")
i = 0  # Inicializa o índice
while i < len(clientes):  # Condição do loop
    if i == 2:  # Verifica se é o terceiro cliente (índice 2)
        break  # Interrompe o loop
    envia_email(clientes[i])  # Envia o email
    i += 1  # Incrementa o índice

# ---------------------------
# Exemplo 5: Usando while e continue para pular o terceiro cliente
# ---------------------------
print("\nExemplo 5: Enviando email para todos, exceto o 3º (usando continue)")
i = 0  # Inicializa o índice
while i < len(clientes):  # Condição do loop
    if i == 2:  # Verifica se é o terceiro cliente (índice 2)
        i += 1  # Incrementa o índice e pula esta iteração
        continue  # Pula o envio do email para o terceiro cliente
    envia_email(clientes[i])  # Envia o email para os outros clientes
    i += 1  # Incrementa o índice para o próximo cliente

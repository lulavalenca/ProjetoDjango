idade = int(input("Digite a sua idade: "))
if idade >= 18:
    print(f"Voce é maior de idade: {idade} anos.")
else:
    print(f"Você é menor de idade: {idade} anos.") 
    
#Solicita ao usuário que digite a idade do competidor
idade = int(input("Digite a idade do competidor: "))

# Classifica o competidor em uma categoria
if 7 <= idade <= 9:
    categoria = "Mirim"
elif 10 <= idade <= 12:
    categoria = "Infantil"
elif 13 <= idade <= 15:
    categoria = "Juvenil"
elif 16 <= idade <= 17:
    categoria = "Cadete"
elif idade >= 18:
    categoria = "Adulto"
else:
    categoria = "Idade fora da faixa permitida para competição."
    
# Exibe a categoria do competidor
print(f"O competidor de {idade} anos esta na categoria: {categoria}.")                        
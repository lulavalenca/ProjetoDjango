# Solicita ao usuario que digite tres numeros
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

#
if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maior = numero2
else:
    maior = numero3

# Exibe o maior numero
print(f"O maior numero é: {maior}")            
# Verifica dois números, mostra qual é maior e depois os soma

num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))
somaNum = num1 + num2
if num1 > num2:
    print(f"{num1} é maior que {num2}.")
elif num1 < num2:
    print(f"{num2} é maior que {num1}.")
else:
    print("Os números são iguais.")
print(f"A soma de {num1} com {num2} é {somaNum}.")
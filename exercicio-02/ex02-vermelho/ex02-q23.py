# Exibe, em ordem decrescente, o resto da divisão por 3 de três números

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))
r1 = num1 % 3
r2 = num2 % 3
r3 = num3 % 3
if r1 > r2:
    if r2 > r3:
        print(f"{r1}, {r2}, {r3}.")
    else:
        print(f"{r1}, {r3}, {r2}.")
elif r2 > r1:
    if r1 > r3:
        print(f"{r2}, {r1}, {r3}.")
    else:
        print(f"{r2}, {r3}, {r1}.")
else:
    if r1 > r2:
        print(f"{r3}, {r1}, {r2}.")
    else:
        print(f"{r3}, {r2}, {r1}.")
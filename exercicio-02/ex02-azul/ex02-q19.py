# Verifica se dois números são iguais ou diferentes e, caso diferentes, os subtrai

num1 = float(input("Insira um número: "))
num2 = float(input("Insira um número: "))
if num1 == num2:
    print("São iguais.")
else:
    diferencaNum = num1 - num2
    print(f"São distintos e a diferença é igual a {diferencaNum}.")
# Informa se número é positivo ou negativo

num = int(input("Insira um número: "))
if num > 0:
    print(f"{num} é um número positivo.")
elif num < 0:
    print(f"{num} é um número negativo.")
else:
    print(f"{num} é zero.")
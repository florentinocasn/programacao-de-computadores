# Verifica se um número é par positivo, par negativo, ímpar positivo, ímpar negativo ou neutro

num = int(input("Insira um número: "))
if num == 0:
    print("Número neutro.")
elif num % 2 == 0:
    if num > 0:
        print("Par positivo.")
    else:
        print("Par negativo.")
else:
    if num > 0:
        print("Ímpar positivo.")
    else:
        print("Ímpar negativo.")
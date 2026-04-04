# Verifica se um número é par positivo, par negativo ou ímpar

num = int(input("Insira um número: "))
if num == 0:
    print("Insira um valor diferente de zero.")
elif num % 2 == 0:
    if num > 0:
        print("Par positivo.")
    else:
        print("Par negativo.")
else:
    print("Ímpar.")
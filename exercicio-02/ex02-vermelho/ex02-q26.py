# Lê um número inteiro e o classifica em "pequeno", "médio", "grande" ou "nagativo ou zero"

num = int(input("Insira um número: "))
if num > 0:
    if num < 10:
        print("Pequeno.")
    else:
        if num >= 10 and num < 100:
            print("Médio.")
        else:
            print("Grande.")
else:
    print("Negativo ou zero.")
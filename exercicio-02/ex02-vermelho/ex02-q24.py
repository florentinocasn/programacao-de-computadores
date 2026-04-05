# Verifica se um número inteiro está no intervalo de 1 a 100 e, se estiver, se é par ou ímpar

num = int(input("Insira um número: "))
if num >= 0 and num <= 100:
    if num % 2 == 0:
        print("Par no intervalo.")
    else:
        print("Ímpar no intervalo.")
else:
    print("Fora do intervalo.")
# Verifica se um número é positivo e se é múltiplo de 2 e de 3 ao mesmo tempo

num = int(input("Insira um número: "))
if num > 0 and num % 2 == 0 and num % 3 == 0:
    print("Múltiplo de 2 e 3.")
elif num <= 0:
    print("Número inválido.")
else:
    print("Não atende.")
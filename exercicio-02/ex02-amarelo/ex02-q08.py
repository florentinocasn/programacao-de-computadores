# Calcula a raiz aproximada se um número for positivo

num = float(input("Insira um número: "))
if num > 0:
    raizNum = num ** 0.5
    print(f"A raiz aproximada de {num} é {raizNum}.")
else:
    print("Número inválido.")
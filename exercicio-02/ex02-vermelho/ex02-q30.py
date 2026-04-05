# Verifica um valor e, se for um número inteiro, verifica se é par e maior ou menor que 100, ou ímpar

valor = input("Insira um valor: ")
if valor.isdigit():
    conversao = int(valor)
    if conversao % 2 == 0:
        if conversao > 100:
            print("Par alto.")
        else:
            print("Par baixo.")
    else:
        print("Ímpar.")
else:
    print("Entrada inválida.")
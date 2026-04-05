# Tenta converter um valor para inteiro e, caso seja bem-sucedido, classifica o número em "alto" ou "baixo"

valor = input("Insira um valor: ")
if valor.isdigit():
    conversao = int(valor)
    if conversao > 10:
        print("Alto.")
    else:
        print("Baixo.")
else:
    print("Entrada inválida.")
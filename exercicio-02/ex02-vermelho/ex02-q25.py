# Verifica o tipo de um valor e se é possível convertê-lo para real e dividí-lo por 2

valor = input("Insira um valor: ")
print("Tipo da variável: ", type(valor))
if valor.isdigit():
    conversao = float(valor)
    divisao = conversao / 2
    print(f"A metade de {valor} é: ", divisao)
else:
    print("Não numérico.")
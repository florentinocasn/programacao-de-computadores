# Verifica o tipo da variável e, se for um valor numérico, exibe o dobro se for inteiro, ou a metade se for real

valor = input("Insira um valor: ")
print("Tipo da variável: ", type(valor))
try:
    numero = float(valor)
    if numero.is_integer():
        print(f"O dobro de {valor} é: ", numero * 2)
    else:
        print(f"A metade de {valor} é: ", numero / 2)
except:
    print("Tipo inválido.")
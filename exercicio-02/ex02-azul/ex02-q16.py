# Classifica o tipo de um valor e, se for numérico, mostra o quadrado

valor = input("Insira um valor: ")
valorTipo = type(valor)
print(valorTipo)
if valorTipo == int or float:
    valorQuadrado = float(valor) ** 2
    print(valorQuadrado)
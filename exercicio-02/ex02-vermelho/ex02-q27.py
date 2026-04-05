# Lê dois números e calcula a soma se forem positivos, ou o produto se forem negativos

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

if num1 > 0 and num2 > 0:
    soma = num1 + num2
    print(f"A soma de {num1} e {num2} é: ", soma)
elif num1 < 0 and num2 < 0:
    produto = num1 * num2
    print(f"O produto de {num1} e {num2} é: ", produto)
else:
    print("Tente novamente.")
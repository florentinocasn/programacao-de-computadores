# Mostra a metade de um número caso este seja maior que 100, senão, mostra o dobro.

num = float(input("Insira um número: "))
if num > 100:
    metadeNum = num / 2
    print(f"A metade de {num} é {metadeNum}.")
else:
    dobroNum = num * 2
    print(f"O dobro de {num} é {dobroNum}.")
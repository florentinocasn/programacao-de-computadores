# Verifica se um número está entre 0 e 100 e, caso esteja fora do intervalo, mostra na tela

num = float(input("Insira um número: "))
if num <= 0 or num >= 100:
    print(num)
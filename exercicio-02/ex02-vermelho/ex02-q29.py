# Verifica se um número é múltiplo de cinco e, se for, o classifica em alto ou baixo

num = int(input("Insira um número: "))
if num % 5 == 0:
    if num > 50:
        print("Múltiplo alto.")
    else:
        print("Múltiplo baixo.")
else:
    print("Não é múltiplo de 5.")
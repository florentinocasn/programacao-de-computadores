# Verifica se um número é múltiplo de três

num = int(input("Insira um número: "))
if num == 0:
    print("Insira um valor diferente de zero.")
elif num % 3 == 0:
    print("Múltiplo de 3.")
else:
    print("Não é múltiplo de 3.")
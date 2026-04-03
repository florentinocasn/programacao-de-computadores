# Informa se um número é ímpar ou par

num = int(input("Insira um número: "))
if num == 0:
    print(f"{num} é zero.")
elif num % 2 == 0:
    print(f"{num} é um número par.")
else:
    print(f"{num} é um número ímpar.")
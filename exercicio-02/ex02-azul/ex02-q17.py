# Verifica se um indivíduo é menor de idade, adulto ou idoso

idade = float(input("Insira uma idade: "))
if idade < 0:
    print("Insira uma idade válida.")
elif idade < 18:
    print("Menor de idade.")
elif idade < 60:
    print("Adulto.")
else:
    print("Idoso.")
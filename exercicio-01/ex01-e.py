# e) Construa um algoritmo que receba a altura e o peso de uma pessoa e calcule o Índice de Massa
# Corporal (IMC).

# Calcula o Índice de Massa Corporal (IMC) de acordo com a altura e peso
altura = float(input("Insira sua altura (em metros): "))
peso = float(input("Insira seu peso (em quilogramas): "))
imc = peso / (altura ** 2)
print("Seu Índice de Massa Corporal (IMC) é:", imc)
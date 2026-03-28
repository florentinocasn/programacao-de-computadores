# Programação de Computadores

# Docente: Joanacelle Caldas de Melo
# Discente: Florentino Cazé de Andrade Segundo Neto
# Turma: B

# Exercício 01

# a) Elabore um algoritmo que receba dois números, calcule a multiplicação entre eles e apresente o
# resultado.

# Recebe dois números e os multiplica
valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))
multiplicacao = valor1 * valor2
print("O resultado da multiplicação é:", multiplicacao)

# b) Desenvolva um algoritmo que receba cinco números, calcule a média aritmética e apresente o
# resultado final.

# Recebe cinco números e calcula a média aritmética entre eles
valorA = float(input("Digite o primeiro valor: "))
valorB = float(input("Digite o segundo valor: "))
valorC = float(input("Digite o terceiro valor: "))
valorD = float(input("Digite o quarto valor: "))
valorE = float(input("Digite o quinto valor: "))
mediaAritmetica = (valorA + valorB + valorC + valorD + valorE) / 5
print("O resultado da média aritmética é:", mediaAritmetica)

# c) Construa um algoritmo que receba o valor de um produto e calcule o preço final considerando um
# acréscimo de 8% de imposto.

# Recebe o valor do produto e calcula o preço final com adição de 8% de imposto
valorProduto = float(input("Insira o valor do produto: "))
precoFinal = valorProduto * 1.08
print("O preço final do produto é:", precoFinal)

# d) Elabore um algoritmo que receba dois números e apresente o resultado da subtração entre eles.

# Recebe dois números e os subtrai
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
subtracao = num1 - num2
print("O resultado da subtração é:", subtracao)

# e) Construa um algoritmo que receba a altura e o peso de uma pessoa e calcule o Índice de Massa
# Corporal (IMC).

# Calcula o Índice de Massa Corporal (IMC) de acordo com a altura e peso
altura = float(input("Insira sua altura (em metros): "))
peso = float(input("Insira seu peso (em quilogramas): "))
imc = peso / (altura ** 2)
print("Seu Índice de Massa Corporal (IMC) é:", imc)

# f) Elabore um algoritmo que receba a temperatura em graus Celsius e apresente o valor convertido
# para graus Fahrenheit.

# Converte o valor da temperatura em graus Celsius para Fahrenheit
tempCels = float(input("Insira o valor da temperatura em graus Celsius: "))
tempFahr = (tempCels * 1.8) + 32
print("O valor da temperatura em graus Fahrenheit é:", tempFahr)

# g) Construa um algoritmo que receba a quantidade de horas trabalhadas por um funcionário e o valor
# da hora trabalhada, calculando o salário total.

# Calcura o salário total de acordo com o valor das horas trabalhadas
horasTrabalhadas = float(input("Insira a quantidade de horas trabalhadas: "))
valorHora = float(input("Insira o valor por hora trabalhada: "))
salarioTotal = horasTrabalhadas * valorHora
print("Seu salário total é:", salarioTotal)
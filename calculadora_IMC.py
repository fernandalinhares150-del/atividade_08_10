peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Calcula o IMC
imc = peso / (altura * altura)

# Classifica o IMC
if imc < 18.5:
    print("IMC:", round(imc, 2), "— Abaixo do peso")
elif imc < 25:
    print("IMC:", round(imc, 2), "— Peso normal")
elif imc < 30:
    print("IMC:", round(imc, 2), "— Sobrepeso")
else:
    print("IMC:", round(imc, 2), "— Obesidade")

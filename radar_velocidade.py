# Entrada
velocidade = float(input("Digite a velocidade: "))

# Decisão: verifica se passou de 80 km/h
if velocidade > 80:
    # Calcula quanto passou do limite
    excesso = velocidade - 80
    print("Multado! Você passou", excesso, "km/h do limite.")
else:
    print("Velocidade dentro do limite. Boa viagem!")

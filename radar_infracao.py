limite = float(input("Digite o limite de velocidade: "))
velocidade = float(input("Digite a velocidade medida: "))

# Verifica se não passou do limite
if velocidade <= limite:
    print("Sem infração")
else:
    # Calcula o percentual acima do limite
    percentual = (velocidade - limite) / limite * 100

    # Classifica a infração
    if percentual <= 20:
        print(round(percentual, 2), "% acima — Infração média")
    elif percentual <= 50:
        print(round(percentual, 2), "% acima — Infração grave")
    else:
        print(round(percentual, 2), "% acima — Infração gravíssima")


saque = int(input("Digite o valor do saque: "))

# Verifica se o valor é válido
if saque <= 0 or saque % 10 != 0:
    print("Valor inválido para saque")
else:
    # Calcula as notas de 100
    qtd100 = saque // 100
    resto = saque % 100

    # Calcula as notas de 50
    qtd50 = resto // 50
    resto = resto % 50

    # Calcula as notas de 20
    qtd20 = resto // 20
    resto = resto % 20

    # Calcula as notas de 10
    qtd10 = resto // 10

    # Mostra somente as notas usadas
    if qtd100 > 0:
        print(qtd100, "nota(s) de R$ 100")

    if qtd50 > 0:
        print(qtd50, "nota(s) de R$ 50")

    if qtd20 > 0:
        print(qtd20, "nota(s) de R$ 20")

    if qtd10 > 0:
        print(qtd10, "nota(s) de R$ 10")
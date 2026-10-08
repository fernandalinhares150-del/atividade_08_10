saldo = float(input("Digite o saldo: "))
saque = float(input("Digite o valor do saque: "))

# Verifica se existe saldo suficiente
if saldo >= saque:
    # Calcula o novo saldo
    novo_saldo = saldo - saque
    print("Saque realizado. Novo saldo: R$", novo_saldo)
else:
    print("Saldo insuficiente")

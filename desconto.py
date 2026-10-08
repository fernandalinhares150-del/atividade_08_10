compra = float(input("Digite o valor da compra: "))

# Verifica se a compra tem direito ao desconto
if compra >= 100:
    # Calcula 10% de desconto
    desconto = compra * 0.10
    valor_final = compra - desconto
else:
    # Sem desconto
    valor_final = compra

# Saída
print("Valor final: R$", valor_final)

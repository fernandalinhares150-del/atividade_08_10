compra = float(input("Digite o valor da compra: "))

# Define o percentual de desconto
if compra < 50:
    desconto = 0
elif compra < 100:
    desconto = 0.05
elif compra < 200:
    desconto = 0.10
else:
    desconto = 0.15

# Calcula o desconto e o valor final
valor_desconto = compra * desconto
valor_final = compra - valor_desconto

print("Desconto: R$", valor_desconto, "— Final: R$", valor_final)

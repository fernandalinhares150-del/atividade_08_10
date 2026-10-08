# Entrada: lê o preço e a quantidade do produto
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade: "))
dinheiro = float(input("Digite o valor pago: "))

# Processamento: calcula o total e o troco
total = preco * quantidade
troco = dinheiro - total

# Saída: mostra o total e o troco
print("Total da compra: R$", total)
print("Troco: R$", troco)

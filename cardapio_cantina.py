print("1 - Pão de queijo: R$ 4.50")
print("2 - Coxinha: R$ 6.00")
print("3 - Pastel: R$ 7.00")
print("4 - Suco: R$ 5.00")
print("5 - Café: R$ 3.00")

# Entrada
codigo = int(input("Digite o código: "))
quantidade = int(input("Digite a quantidade: "))

# Escolhe o preço
if codigo == 1:
    preco = 4.50
elif codigo == 2:
    preco = 6.00
elif codigo == 3:
    preco = 7.00
elif codigo == 4:
    preco = 5.00
elif codigo == 5:
    preco = 3.00
else:
    print("Código inválido")
    exit()

# Calcula o total
total = preco * quantidade

print("Total: R$", total)

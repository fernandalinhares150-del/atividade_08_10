
# Entrada
dividendo = float(input("Digite o dividendo: "))
divisor = float(input("Digite o divisor: "))

# Decisão: verifica se o divisor é zero
if divisor == 0:
    print("Erro: não existe divisão por zero")
else:
    # Processamento: calcula a divisão
    resultado = dividendo / divisor

    # Saída
    print("Resultado:", resultado)

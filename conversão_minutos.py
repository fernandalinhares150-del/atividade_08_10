# Entrada: lê a quantidade de minutos
total_minutos = int(input("Digite a quantidade de minutos: "))

# Processamento: calcula as horas e os minutos restantes
horas = total_minutos // 60
minutos = total_minutos % 60

# Saída: mostra o resultado
print("Horas:", horas)
print("Minutos:", minutos)

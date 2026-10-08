# Entrada: lê as duas notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Processamento: calcula a média
media = (nota1 + nota2) / 2

# Saída: mostra a média
print("Média:", media)

# Verifica se o aluno foi aprovado
if media >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média
media = (nota1 + nota2) / 2

# Verifica a situação do aluno
if media >= 7:
    print("Média", media, "— Aprovado")
elif media >= 5:
    print("Média", media, "— Recuperação")
else:
    print("Média", media, "— Reprovado")

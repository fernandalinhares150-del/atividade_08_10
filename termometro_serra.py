temperatura = float(input("Digite a temperatura: "))

# Classifica a temperatura
if temperatura < 0:
    print("Abaixo de zero — risco de geada!")
elif temperatura < 10:
    print("Muito frio — capriche no agasalho")
elif temperatura < 18:
    print("Frio")
elif temperatura < 25:
    print("Agradável")
else:
    print("Calor")
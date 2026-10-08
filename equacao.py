a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Verifica se é uma equação do segundo grau
if a == 0:
    print("Não é uma equação do 2º grau")
else:
    # Calcula o delta
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Não existem raízes reais")

    elif delta == 0:
        # Existe uma raiz
        x = -b / (2 * a)
        print("Uma raiz: x =", x)

    else:
        # Existem duas raízes
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)

        print("x1 =", x1, "e x2 =", x2)
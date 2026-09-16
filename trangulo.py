# Programa para verificar e classificar triângulos

# Entrada dos lados
a = float(input("Digite o valor do lado a: "))
b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))

# Verificação da condição de existência do triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    # Classificação do triângulo
    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Erro: os valores informados não formam um triângulo válido.")

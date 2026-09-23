# contrua um programa onde o usuario digitara cinco numeros e o programa devera colocar
# esses numeros dentro do vetor em ordem crescente 

numeros = []
print("digite 5 mumeros")
for i in range (0,5):
    num =int(input(f"digite o {i} numero:"))
numeros.append(num)

# Ordenando a lista
numeros.sort()

# Exibindo resultado
print("Números em ordem crescente:", numeros)
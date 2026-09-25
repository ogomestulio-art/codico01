# subisittuir numeros inteiros negativos 

vetor = []
for i in range(0,10):
    numero = int(input(f"digite o {i+1} numero inteiro:"))
    vetor.append(numero)

# substituido valores negativos por zero 
for i in range(10):
    if vetor[i] < 0: 
        vetor[i] = 0

    # Exiba o vetor final 
    print("\nVetor final após substituição:")
for valor in vetor:
    print(valor, end=" ")
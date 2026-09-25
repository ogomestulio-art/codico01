vetor = []
for i in range(0,8):
    numero = float(input(f"digite o {i+1} numero:"))
    vetor.append(numero)

    # numeros presente no vetor
    busca = int(input("\ndigite um numero para verificar se esta no vetor"))

   #verificando se o nuemero esta presente 
    for i in range(8):
        if vetor[i] == busca:
            print(f"o numero {busca} foi encontrado na posição (indice) {i}.")
            encontrado = True
            break # encerra ao econtrar a primeira ocorrencia
        if not encontrado:
            print(f" o numero {busca} não esta presente no vetor")
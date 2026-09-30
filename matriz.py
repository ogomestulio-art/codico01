# Construa uma matriz 2X2 e, como saída desse programa, a média e a soma
# dos valores digitados deverão ser calculadas.

matriz = []
print("digite o valor para uma matriz 2x2:")

# loop para ler os dados da linha e coluna 
for i in range(2): # linha
    linha = [] # elemnetos da linha
    for j in range(2): # para cada elemento da linha
        valor = float(input(f"digite o valor para posição [{i}][{j}]:"))
    linha.append(valor)  # quando acabar de ler guarde na matriz
    matriz.append(linha)
    
    # calculos da soma e da media
    soma = 0
    for linha in matriz:
        soma += sum(linha)
        
        total_elementos = 4
        media = soma / total_elementos
        
        # exibir os resultados
        print("\nmatriz digitada:")
        for linha in matriz:
            print(linha)
            
            print(f"\media dos valores: {media}")
            
             
    

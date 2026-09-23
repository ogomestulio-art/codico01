# contrua um programa onde o usuario digitara sete numeros e o programa escreverá, na tela quantos deles são pares
# e quantos são impares.

numeros = []
print("digite 7 mumeros")
for i in range (0,7):
    num =int(input(f"digite o {i} numero:"))
    numeros.append(num)

pares = 0
impares = 0

for num in numeros :
    if num % 2 == 0:
        pares +=1
    else:
        impares += 1

print("\n--- resultado---")
print(f" os numeros digitados foram :{numeros}")
print(f"quantiades de nuemros pares:{pares}")
print(f"quantidade de numeros impares:{impares}")




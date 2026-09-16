# digite seu número
# criar a tabuda do numero até 10

numero = int(input('fale a tabuada que deseja prender'))

for i in range(0, 10) :
    resultado= numero * (i + 1)
    print(f'{numero} * {i+1} = {resultado}') 
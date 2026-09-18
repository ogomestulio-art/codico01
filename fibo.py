# calcular a sequencia de fibonacci ate 2000
# não tem entrda de usuario 

anterior = 0
atual = 1
proximo = anterior + atual #1 
print(anterior)
print(atual)
print(proximo)
while(atual <= 2000) :
    anterior = atual
    atual = proximo
    proximo = anterior + atual
    print(proximo)
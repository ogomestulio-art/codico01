lista = []
for i in range(0,4):
    aluno = input("digite o nome do aluno:")
    nota = float(input("digite a media do aluno:"))
    lista.append([aluno, nota])

    for aluno_nota in lista:
        if aluno[1] >= 6:
            print(aluno[0])

        # for i in rang(0, len(lista)): versão 2
        # if lista[i][1] >=6:
        # print(lista[i][0])    
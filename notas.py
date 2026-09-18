# solicitar nota ao usuario
nota1 = float(input("digite a nota do aluno:"))
nota2 = float(input("digite a nota do aluno:"))

# criar media aritmetica
media = (nota1 + nota2) / 2
print("a media do aluno é:", media)

# verificar a condição de aprovação
if media >= 6:
        print("o aluno foi aprovado")
else:
        print("o aluno foi reprovado")


# solicitar nota ao usuario
nota1 = float(input("digite a nota do aluno:"))
nota2 = float(input("digite a nota do aluno:"))

# criar media aritmetica
media = (nota1 + nota2) / 2
print("a media do aluno é:", media)

# verificar a condição de aprovação
if media < 6:
        print("o aluno reprovado")
else:
        print("o aluno foi aprovado")
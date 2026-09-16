
# criar variáveis de concessão de empréstimo
renda_mensal = 4500
score = 750
possui_restricao = False

# lógica de avaliação de empréstimo
if score >= 700 and renda_mensal >= 4000:
    status = 'aprovado'

elif renda_mensal >= 2500 and not possui_restricao :
    status ='reprovado'

else:
    status = 'reprovado'

print(status)
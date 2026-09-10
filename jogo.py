# importar as bibliotecas necessárias
import random
def jogar():

# criar uma lista com três opções de jogo
    opcoes = ["pedra", "papel", "tesoura"]
# solicitar a escolha do usuário
    escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
    
# verificar se a escolha do usuário é válida
    if escolha_usuario not in opcoes:
        print("Escolha inválida. Tente novamente.")
        return

# o computador faz uma escolha aleatória
    escolha_computador = random.choice(opcoes)
    
# mostrar as escolhas do usuário e do computador
print("Você escolheu:", escolha_usuario)
print("O computador escolheu:", escolha_computador)

# caso 1 se ou escolha do usuário for igual a escolha do computador o jogo é empate
if escolha_usuario == escolha_computador: 
    print("Empate!")

# caso 2: testar  todas as combinações possiveis de vitória do usuário
elif(usuario == 'pedra' and computador == 'tesoura') or \
    (usuario == 'tesoura' and computador == 'papel') or \
    (usuario == 'papel' and computador == 'pedra'  ) or \  
print("Você venceu!") 

# caso 3:se não for empate e nem vitória do usuário, o computador vence
else:
print("O computador venceu!")
    
# Executa a função para o jogo rodar
jogar()
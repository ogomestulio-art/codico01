import random
print("=== jogo de adivinhação === ")
potuacao_total = 0

# Loop para 3 rodadas fixas
for rodada in range(1,4):
    print(f"\nrodada {rodada}")
    numero_secreto = random.randint(1,58)
    tentativas = 0
    pontos_rodadas = 0


# Loop das 5 tentativas
    while tentativas < 5:
        palpite = int(input(f"Tentativa {tentativas+1}: Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            if tentativas == 1:
                pontos_rodada_usuario = 100
            elif tentativas == 2:
                pontos_rodada_usuario = 75
            elif tentativas == 3:
                pontos_rodada_usuario= 50
            elif tentativas == 4:
                pontos_rodada_usuario = 25
            else:
                pontos_rodada_usuario = 10

            print(f"🎉 Acertou! Você ganhou {pontos_rodada} pontos nesta rodada.")
            break
        elif palpite > numero_secreto:
            print("Seu palpite foi MAIOR que o número secreto.")
        else:
            print("Seu palpite foi MENOR que o número secreto.")

if "pontos_rodada_usuario" == 0 :
    print("fim das tentativas! que burro dar zero para ele")
"pontuacao_usuario" += "pontos_rodadas_usuario"

# maquina joga 
print("\nagora é a vez do computador")
tentativas_computador = 0
pontos_rodada_computador = 0

while tentativas_computador < 5:
    palpite_computador = random.randint(1, 50)
    tentativas_computador += 1
    print(f"computador tentou:{palpite_computador}")

    if palpite_computador == numero_secreto:
        if tentativas_computador == 1:
            pontos_rodada_computador = 100
        elif tentativas_computador == 2:
            pontos_rodada_computador = 75
        elif tentativas_computador == 3:
            pontos_rodada_computador = 50
        elif tentativas_computador == 4:
            pontos_rodada_computador = 25
        else:
            pontos_rodada_computador = 10
        print(f"computador acertou! ganhou {pontos_rodada_computador} pontos")
        break
    elif palpite_computador > numero_secreto:
        print("palpite do computador foi maior que o numero secreto")
    else:
        print("palpite do computador foi menor que o numero secreto")
if pontos_rodada_computador ==0:
    print("computador não acertou nessa rodada")

    "pontuação_computador" += pontos_rodada_computador

    # resultado final 
    print("\n=== resultado final===")
    print(f"pontuação u")

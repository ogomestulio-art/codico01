import random

print("=== Jogo de Adivinhação ===")
print("Você terá 3 rodadas contra a máquina!")
print("Em cada rodada, tente adivinhar o número secreto entre 1 e 50.\n")

pontuacao_total = 0

# Loop das 3 rodadas
for rodada in range(1, 4):
    print(f"\n--- Rodada {rodada} ---")
    numero_secreto = random.randint(1, 50)
    tentativas = 0
    pontos_rodada = 0

    # Loop das 5 tentativas
    while tentativas < 5:
        palpite = int(input(f"Tentativa {tentativas+1}: Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            if tentativas == 1:
                pontos_rodada = 100
            elif tentativas == 2:
                pontos_rodada = 75
            elif tentativas == 3:
                pontos_rodada = 50
            elif tentativas == 4:
                pontos_rodada = 25
            else:
                pontos_rodada = 10

            print(f"🎉 Acertou! Você ganhou {pontos_rodada} pontos nesta rodada.")
            break
        elif palpite > numero_secreto:
            print("Seu palpite foi MAIOR que o número secreto.")
        else:
            print("Seu palpite foi MENOR que o número secreto.")

    if pontos_rodada == 0:
        print(f"❌ Você não acertou em 5 tentativas. Pontos nesta rodada: 0")

    pontuacao_total += pontos_rodada

# Avaliação final
print("\n=== Resultado Final ===")
print(f"Sua pontuação total foi: {pontuacao_total}")

if pontuacao_total > 200:
    print("🏆 Classificação: Excelente!")
elif 100 <= pontuacao_total <= 200:
    print("👍 Classificação: Bom!")
else:
    print("🙃 Classificação: Tente Novamente!")

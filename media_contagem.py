notas = []
for i in range(6):
    numero = float(input(f"digite o {i+1} numero:"))
    notas.append(numero)

    
# criar media aritmetica
media = sum(notas) /len(notas)

# notas acima da media 
acima_media = []
for i in range(6):
    if notas[i] > media:
        media.append(notas[i])

# exibir resultado 
print(f"\nmedia das notas:{media:.2f}")
print(f"quantidades de notas acima da media: {len(acima_media)}")

if len(media) > 0:
    print("notas acima da nedia:")
    for nota in media:
        print(nota)
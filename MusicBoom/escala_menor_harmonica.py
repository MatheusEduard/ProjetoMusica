def escala_menor_harmonica(nota):
    notas = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C']
    escala = []
    for i in range(len(notas)-25):
        if notas[i] == nota:
            atual = notas[i]
            escala.append(atual)
            atual = notas[i+2]
            escala.append(atual)
            atual = notas[i+3]
            escala.append(atual)
            atual = notas[i+5]
            escala.append(atual)
            atual = notas[i+7]
            escala.append(atual)
            atual = notas[i+8]
            escala.append(atual)
            atual = notas[i+11]
            escala.append(atual)
            atual = notas[i+12]
            escala.append(atual)
            atual = notas[i+14]
            escala.append(atual)
            atual = notas[i+15]
            escala.append(atual)
            atual = notas[i+17]
            escala.append(atual)
            atual = notas[i+19]
            escala.append(atual)
            atual = notas[i+20]
            escala.append(atual)
            atual = notas[i+23]
            escala.append(atual)
            atual = notas[i+24]
            escala.append(atual)
            
    return escala

a=escala_menor_harmonica('C')
print(*a, sep=", ")
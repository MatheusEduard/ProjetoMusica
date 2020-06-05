def escala_maior(nota):
    notas = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C']
    escala = []
    for i in range(len(notas)-25):
        if notas[i] == nota:
            atual = notas[i]
            escala.append(atual)
            atual = notas[i+2]
            escala.append(atual)
            atual = notas[i+4]
            escala.append(atual)
            atual = notas[i+5]
            escala.append(atual)
            atual = notas[i+7]
            escala.append(atual)
            atual = notas[i+9]
            escala.append(atual)
            atual = notas[i+11] +"2"
            escala.append(atual)
            atual = notas[i+12] +"2"
            escala.append(atual)
            atual = notas[i+14]+"2"
            escala.append(atual)
            atual = notas[i+16]+"2"
            escala.append(atual)
            atual = notas[i+17]+"2"
            escala.append(atual)
            atual = notas[i+19]+"2"
            escala.append(atual)
            atual = notas[i+21]+"2"
            escala.append(atual)
            atual = notas[i+23]+"2"
            escala.append(atual)
            atual = notas[i+24]+"2"
            escala.append(atual)
    return escala
            


#print(escala_maior('C'))              

#37 -x = 12 37-12 =25


def do():

    escala = ["C","D","E","F","G","A","B","C2","D2","E2","F2","G2","A2","B2"]
    
    return escala


def doSus():
   
   escala = ["C#","D#","F","F#","G#","A#","C","C#2","D#2","F2","F#2","G#2","A#2","C2"]
    
   return escala 


def re():
    
    escala = ["D","E","F#","G","A","B","C#","D2","E2","F#2","G2","A2","B2","C#2"]
    
    return escala
    
def reSus():
    
    escala = ["D#","F","G","G#","A#","C","D","D#2","F2","G2","G#2","A#2","C2","D2"]
    
    return escala
    
def mi():
    
    escala = ["E","F#","G#","A","B","C#","D#","E2","F#2","G#2","A2","B2","C#2","D#2"]
    
    return escala
    
def fa():
    
    escala = ["F","G","A","A#","C","D","E","F2","G2","A2","A#2","C2","D2","E2"]
    
    return escala
    
def faSus():
    
    escala = ["F#","G#","A#","B","C#","D#","F","F#2","G#2","A#2","B2","C#2","D#2","F2"]
    
    return escala
    
def sol():
    
    escala = ["G","A","B","C","D","E","F#","G2","A2","B2","C2","D2","E2","F#2"]
    
    return escala

def solSus():
    
    escala = ["G#","A#","C","C#","D#","F","G","G#2","A#2","C2","C#2","D#2","F2","G2"]
    
    return escala
    
def la():
    
    escala = ["A","B","C#","D","E","F#","G#","A2","B2","C#2","D2","E2","F#2","G#2"]
    
    return escala
    
def laSus():
    
    escala = ["A#","C","D","D#","F","G","A","A#2","C2","D2","D#2","F2","G2","A2"]
    
    return escala
    
def si():
    
    escala = ["B","C#","D#","E","F#","G#","A#","B2","C#2","D#2","E2","F#2","G#2","A#2"]
    
    return escala

#print(*doSus(), sep=", ") x -15 = 6
    

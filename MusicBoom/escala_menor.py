def escala_menor(nota):
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
            atual = notas[i+10]
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
            atual = notas[i+22]
            escala.append(atual)
            atual = notas[i+24]
            escala.append(atual)
    return escala

#a=escala_menor('D#')
#print(*a, sep=', ')

def do():

    escala = ["C","D","D#","F","G","G#","A#","C"]
    
    return escala


def doSus():
   
   escala = ["C#","D#","E","F#","G#","A","B","C#"]
    
   return escala 


def re():
    
    escala = ["D","E","F","G","A","A#","C","D"]
    
    return escala
    
def reSus():
    
    escala = ["D#","F","F#","G#","A#","B","C#","D#"]
    
    return escala
    
def mi():
    
    escala = ["E","F#","G","A","B","C","D","E"]
    
    return escala
    
def fa():
    
    escala = ["F","G","G#","A#","C","C#","D#","F"]
    
    return escala
    
def faSus():
    
    escala = ["F#","G#","A","B","C#","D","E","F#"]
    
    return escala
    
def sol():
    
    escala = ["G","A","A#","C","D","D#","F","G"]
    
    return escala

def solSus():
    
    escala = ["G#","A#","B","C#","D#","E","F#","G#"]
    
    return escala
    
def la():
    
    escala = ["A","B","C","D","E","F","G","A"]
    
    return escala
    
def laSus():
    
    escala = ["A#","C","C#","D#","F","F#","G#","A#"]
    
    return escala
    
def si():
    
    escala = ["B","C#","D","E","F#","G","A","B"]
    
    return escala

#print(*doSus(), sep=", ")
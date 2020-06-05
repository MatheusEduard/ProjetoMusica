notas = [('C',0.5),('C#',0.5),('D',0.5),('D#',0.5),('E',0.5),('F',0.5),('F#',0.5),('G',0.5),('G#',0.5),('A',0.5),('A#',0.5),('B',0.5),('C2',0.5),('C#2',0.5),('D2',0.5),('D#2',0.5),('E2',0.5),('F2',0.5),('F#2',0.5),('G2',0.5),('G#2',0.5),('A2',0.5),('A#2',0.5),('B2',0.5)]
notas = dict(notas)
prim = "C2"
ter = "F#2" 
tom1=0
tom2=0  
for e in notas.keys():
    if e == prim:
        tom1 = tom1 + notas[e]
        
    if e != ter and tom1 != 0:
        print(e)
        tom1 = tom1 + notas[e]
    
    if e == ter:
        break
tom1 = tom1 - 0.5        
        
print(tom1)
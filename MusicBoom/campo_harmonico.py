from escala_maior import *



def campo_harmonico_maior_triade(nota):
    notas = [('C',0.5),('C#',0.5),('D',0.5),('D#',0.5),('E',0.5),('F',0.5),('F#',0.5),('G',0.5),('G#',0.5),('A',0.5),('A#',0.5),('B',0.5),('C2',0.5),('C#2',0.5),('D2',0.5),('D#2',0.5),('E2',0.5),('F2',0.5),('F#2',0.5),('G2',0.5),('G#2',0.5),('A2',0.5),('A#2',0.5),('B2',0.5)]
    notas = dict(notas)
    escala_nota = ' '
    nota = str(nota)
    #determina a escala maior para a nota
    if nota == 'C':
        escala_nota = do()
    elif nota == 'C#':
        escala_nota = doSus()
    elif nota == 'D':
        escala_nota = re()
    elif nota == 'D#':
        escala_nota = reSus()
    elif nota == 'E':
        escala_nota = mi()
    elif nota == 'F':
        escala_nota = fa()
    elif nota == 'F#':
        escala_nota = faSus()
    elif nota == 'G':
        escala_nota = sol()
    elif nota == 'G#':
        escala_nota = solSus()
    elif nota == 'A':
        escala_nota = la()
    elif nota == 'A#':
        escala_nota = laSus()
    elif nota == 'B':
        escala_nota =si() 
    else:
        print("Essa Nota Não Existe!!!")
     
    #percorre a escala maior, pega a 1°,3° e 5° nota para formar um acorde   
    for i in range(len(escala_nota)-8):
        prim= escala_nota[i]
        ter= escala_nota[i+2]
        quin= escala_nota[i+4]
        #percorrer do prim ao ter e somar os valores
        tom1 = 0
        tom2 = 0
        for e in notas.keys():
            if e == prim:
                tom1 = tom1 + notas[e]
                
            if e != ter and tom1 != 0:
            
                tom1 = tom1 + notas[e]
            
            if e == ter:
                break
        tom1 = tom1 - 0.5
         
        #percorrer do prim ao quin e somar os valores
        for e in notas.keys():
            if e == prim:
                tom2 = tom2 + notas[e]
                
            if e != quin and tom2 != 0:
            
                tom2 = tom2 + notas[e]
            
            if e == quin:
                break
        tom2 = tom2 - 0.5
        
            
            
            
        acorde = ' '
        acordes = []
            
        #dependendo do intervalo de tons ele vai definir o se o acorde é maior ou menor e alterado ou não alterado
        if tom1 == 2.0:
            acorde = str(prim)
                
        elif tom1 == 1.5:
            acorde = str(prim+'m')
        
        else:
            print('invalido')
            print(tom1)
            
                
        if tom2 == 3.5:
            acorde = str(acorde)   
                
        elif tom2 == 3.0:
            acorde = str(acorde+'(b5)')
        
        else:
            print('invalido')
            print(tom1)
                
        acordes.append(acorde)
            
        print(*acordes)
        print("1°: "+prim)
        print("3°: "+ter)
        print("5°: "+quin)
        print("-----------------------------------------")
       
    return acordes   
       
acordes = campo_harmonico_maior_triade('C#')      





        
    


    
    

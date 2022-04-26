import random

palabras = []

f = open("palabras.txt", "r")
for p in f:
    p = p[:-1]
    palabras.append(p)

f.close()

palinc = random.choice(palabras)

def mostrar(g, intentos = 0):
    for l in g:
        print(l, end=" ")
    if intentos == 0:
        print("")
    else:
        print("- intentos: ", intentos)

guiones = "_" * len(palinc)

mostrar(palinc)

mostrar(guiones)
guiones = ["_"] * len(palinc)

intentos = 0

while True:    
    letra = input()
    
    mal = True
    for i,l in enumerate(palinc):
        if l == letra:
            guiones[i] = letra
            mal = False
            
    if mal:
        intentos += 1
        
    mostrar(guiones, intentos)
        
    if "_" not in guiones:
        print("acertaste")
        break
    elif intentos == 7:
        print("perdiste")
        break
    

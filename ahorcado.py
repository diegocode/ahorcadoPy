import random

palabras = []

f = open("palabras.txt", "r")
for p in f:
    p = p[:-1]
    palabras.append(p)

#f = open("palabras.txt", "w")
#f.write("uno\n")
f.close()

palinc = random.choice(palabras)

def mostrar(g):
    for l in g:
        print(l, end=" ")
    print("")

guiones = "_" * len(palinc)

mostrar(palinc)

mostrar(guiones)
guiones = ["_"] * len(palinc)
while True:
    n = 0
    letra = input()
    
    for i,l in enumerate(palinc):
        if l == letra:
            guiones[i] = letra
        
    mostrar(guiones)
        
    if "_" not in guiones:
        break
    
    
  

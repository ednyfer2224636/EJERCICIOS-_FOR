"""Números pares e impares"""

import random
lista = random.randint(1,1000)
y = lista
p = 0
im = 0
print(y)
#rta = "Numeros = ("

for i in range(1, y+1):
    if (i % 2) == 0:
        p = p + 1        
    else:
        im += 1
    
    """if i < (lista-1):
        rta = rta + str(lista) + ", "  
    else: 
        rta = rta + str(lista)
rta = rta + ") "
print(rta)"""

print(f"La cantidad de números pares = {p}")
print(f"La cantidad de números impares = {im}")


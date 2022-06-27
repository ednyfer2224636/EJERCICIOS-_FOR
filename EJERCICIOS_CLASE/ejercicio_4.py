"""Programa que simula el lanzamiento de n dados y que muestre en forma de histograma la frecuencia con la que salio cada uno de los 6 números"""

import random

x=int(input("Digite el número de veces que lanzará el dado: "))

a = ""
b = ""
c = ""
d = ""
e = ""
f = ""

for i in range(x):
    lanzamientos=random.randint(1,6)
    
    if lanzamientos == 1:
        a += "#"
    elif lanzamientos == 2:
        b += "#"
    elif lanzamientos == 3:
        c += "#"
    elif lanzamientos == 4:
        d += "#"
    elif lanzamientos == 5:
        e += "#"
    elif lanzamientos == 6:
        f += "#"
print("El número 1 se muestra " + str(a) + " veces" + "\n" + "El número 2 se muestra " + str(b) + " veces" + "\n" + "El número 3 se muestra " + str(c) + " veces" + "\n" + "El número 4 se muestra " + str(d) + " veces" + "\n" + "El número 5 se muestra " + str(e) + " veces" + "\n" + "El número 6 se muestra " + str(f) + " veces")



"""Programa que genere mil números aleatorios, y que averigüe e imprima cuantos son pares y cuantos impares"""

import random
n = int(input("Digite un número: "))
p = 0
im = 0
rta = "Numeros = ("

for i in range(n):
    lista = random.randint(1,200)
    if (lista % 2) == 0:
        p = p + 1
            
    else:
        im += 1
    if i < (n-1):
        rta = rta + str(lista) + ", "  
    else: 
        rta = rta + str(lista)
rta = rta + ") "
print(rta)
print(f"La cantidad de números pares = {p}")
print(f"La cantidad de números impares = {im}")
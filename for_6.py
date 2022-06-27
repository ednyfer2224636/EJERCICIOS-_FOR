"""Múltiplos de 7 y 9 hay entre 1000 y 5000"""

siete = 0
nueve = 0

for i in range(1000, 5001):
    if i % 7 == 0:
        siete += 1

    if i % 9 == 0:
        nueve += 1

print(f"Números múltiplos de 7: = {siete}, y múltiplos de 9: {nueve}")
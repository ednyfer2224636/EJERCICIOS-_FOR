import random
n = int(input("Digite el número de dados: "))
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
rta = "Lanzamientos = ("

for i in range(n):
    dado = random.randint(1,6)
    if dado == 1:
        a = a + 1
    
    elif dado == 2:
        b = b + 1

    elif dado == 3:
        c = c + 1

    elif dado == 4:
        d = d + 1

    elif dado == 5:
        e = e + 1

    elif dado == 6:
        f = f + 1
    
    else:
        print("Cara no válida")

    if i < (n-1):
        rta = rta + str(dado) + ", "  
    else: 
        rta = rta + str(dado)

rta = rta + ")"

for i in range(a):
    rta = rta + " *"
rta = rta + " >>> " + str(a) 

for i in range(b):
    rta = rta + " *"
rta = rta + " >>> " + str(b) 

for i in range(c):
    rta = rta + " *"
rta = rta + " >>> " + str(c) 

for i in range(d):
    rta = rta + " *"
rta = rta + " >>> " + str(d) 

for i in range(e):
    rta = rta + " *"
rta = rta + " >>> " + str(e) 

for i in range(f):
    rta = rta + " *"
rta = rta + " >>> " + str(f) 

print(rta)
print(f"La cantidad de veces que se repite el 1, es = {a}")
print(f"La cantidad de veces que se repite el 2, es = {b}")
print(f"La cantidad de veces que se repite el 3, es = {c}")
print(f"La cantidad de veces que se repite el 4, es = {d}")
print(f"La cantidad de veces que se repite el 5, es = {e}")
print(f"La cantidad de veces que se repite el 6, es = {f}")

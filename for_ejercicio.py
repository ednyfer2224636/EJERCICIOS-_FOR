# Digitar nombre y contar las vocales
nombre=input("Digite su nombre: ")
a = 0
e = 0
i = 0
o = 0
u = 0

for vocal in nombre:
    if vocal == "a":
        a += 1

    elif vocal == "e":
        e += 1
       
    elif vocal == "i":
        i += 1
        
    elif vocal == "o":
        o += 1
        
    elif vocal == "u":
        u += 1
        
print("Hay", a, "vocales a")
print("Hay", e, "vocales e")
print("Hay", i, "vocales i")
print("Hay", o, "vocales o")
print("Hay", u, "vocales u")
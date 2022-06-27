"""Generar serie: 1, 4, 9, 16, 25, 36 ... n"""

n = int(input("Digite el valor de n: "))

s = "Serie: ("

for i in range(1, n+1):    
    t = i**2
    if i < n:
        s = s + str(t) + ", "  
    else: 
        s = s + str(t)
s = s + ") "
print(s)
"""Generar serie: 2, 6, 12, 20, 30, 42, 46 ... n"""

n = int(input("Digite el valor de n: "))

s = "Serie: ("

for i in range(1, n+1):    
    t = (i**2)+i
    if i < n:
        s = s + str(t) + ", "  
    else: 
        s = s + str(t)
s = s + ") "
print(s)
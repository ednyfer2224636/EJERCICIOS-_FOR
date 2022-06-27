"""Generar serie: 2, 4, 6, 8, 10 ... n"""

n = int(input("Digite el valor de n: "))

s = "Serie: ("

for i in range(1, n+1):    
    t = i
    if i < n:
        s = s + "1/" + str(t) + ", "  
    else: 
        s = s + "1/" + str(t)
s = s + ") "
print(s)
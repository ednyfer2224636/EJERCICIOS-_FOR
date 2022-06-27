"""Generar serie: 1/2, 1/5, 1/10, 1/17, 1/26 ... n"""

n = int(input("Digite el valor de n: "))

s = "Serie: ("

for i in range(1, n+1):    
    t = i ** 2 + 1

    if i < n:
        s = s + "1/" + str(t) + ", "  
    else: 
        s = s + "1/" + str(t)
s = s + ") "
print(s)
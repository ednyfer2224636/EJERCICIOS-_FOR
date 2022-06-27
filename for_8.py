"""Generar la siguiente serie: 1, 2, 3, 4, 5, 6, 7, 8, 9, ...n"""

n = int(input("Digite el valor de n: "))

s = "Serie: ("

for i in range(1, n+1):    
    if i < n:
        s = s + str(i) + ", "  
    else: 
        s = s + str(i)
s = s + ") "
print(s)
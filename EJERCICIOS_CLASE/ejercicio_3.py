"""Programa que lea un número entero y positivo, que calcule su factorial y que lo imprima junto con el número leído"""

x=int(input("Digite un número: "))

fact = 1
for i in range(1,x+1):
    fact = fact*i 
print("El factorial de", x, "es", fact)
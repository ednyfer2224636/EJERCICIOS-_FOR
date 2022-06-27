"""Programa que verigüe e imprima cuantos múltiplos de 7 y de 9 hay en los números comprendidos entre mil y 5mil"""
m = int(input("Digite un número: "))
n = int(input("Digite otro número: "))
siete = 0
nueve = 0
for i in range (m, n+1, 1):
    if (i % 7) == 0:
        siete += 1
    
    if (i % 9) == 0:
        nueve += 1
print(f"Entre {m} y {n} hay" )
print(f"{siete} Múltiplos de 7")
print(f"{nueve} Múltiplos de 9")
" TP 4 ESTRUCTIRAS REPETITIVAS - SENATORE GENARO"

"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""
print("--------------------------------------EJERCICIO N1--------------------------------------")

for N in range(101):
    print(N)
    
"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""
print("--------------------------------------EJERCICIO N2--------------------------------------")

numero : int = int(input("Ingresa un numero entero: "))
contador = 0
if numero == 0:
    contador = 1
else:
    numero = abs(numero)
    while numero > 0:
        numero = numero // 10
        contador+=1

print(f"El numero tiene {contador} digitos")
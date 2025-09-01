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

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""
print("--------------------------------------EJERCICIO N3--------------------------------------")

numero_uno : int = int(input("Ingresa el primer numero: "))
numero_dos : int = int(input("Ingresa el segundo numero: "))

if numero_uno == numero_dos:
    print("No hay numeros de por medio, ambos son iguales")
else:
    if numero_uno > numero_dos:
        numero_uno = numero_uno - 1
        numero_dos = numero_dos + 1
        while numero_uno != numero_dos-1:
            print(numero_dos)
            numero_dos+=1
    else:
        numero_uno = numero_uno + 1
        numero_dos = numero_dos - 1
        while numero_dos != numero_uno-1:
            print(numero_uno)
            numero_uno+=1

"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""
print("--------------------------------------EJERCICIO N4--------------------------------------")

numero : int = int(input("Ingresa un numero entero: "))
suma : int = 0
while numero != 0:
    suma = suma + numero
    numero : int = int(input("Ingresa otro numero entero: "))
    
print(f"La suma de todos los numeros ingresados es: {suma}")

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
print("--------------------------------------EJERCICIO N5--------------------------------------")

import random
Nrand : int = random.randint(0,9)

numero : int = int(input("Adivina el numero entero! Ingresa un numero: "))
intentos : int = 1
while numero != Nrand:
    intentos +=1
    numero : int = int(input("Ups! parece que no adivinaste, prueba de nuevo: "))
    
print(f"Acertaste! el numero era {Nrand} y lo conseguiste en {intentos} intentos")

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""
print("--------------------------------------EJERCICIO N6--------------------------------------")


numero : int = 100
for numero in range(100,-1,-1):
    if numero % 2 == 0:
        print(numero)
        
"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""
print("--------------------------------------EJERCICIO N7--------------------------------------")

numero : int = int(input("ingresa un numero: "))
suma : int = 0
i : int = 0
for i in range(0,numero):
    suma = suma + i + 1
    
print(f"La suma de los numeros comprendidos entre 0 y {numero} es :{suma}")


"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""
print("--------------------------------------EJERCICIO N8--------------------------------------")

N = 100  
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(N):
    numero = int(input(f"Ingrese el número {i+1}: "))


    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Cantidad de pares: {pares}")
print(f"Cantidad de impares: {impares}")
print(f"Cantidad de positivos: {positivos}")
print(f"Cantidad de negativos:  {negativos}")

"""9)"""
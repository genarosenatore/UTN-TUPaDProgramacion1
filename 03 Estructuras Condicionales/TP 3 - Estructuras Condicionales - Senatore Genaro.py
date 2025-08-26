# Práctico 3: Estructuras condicionales
# Alumno: Senatore Genaro

print("\n---------------------------Ejercicio 1---------------------------\n")

""" 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. """

edad : int = int(input("Ingrese su edad para verificar si es mayor de edad: "))
if edad > 18:
    print("Es mayor de edad")

print("\n---------------------------Ejercicio 2---------------------------\n")
    
""" 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”. """    

nota : float = float(input("ingrese su nota para conocer su condicion: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    
print("\n---------------------------Ejercicio 3---------------------------\n")
    
""" 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar. """

numero : int = int(input("Ingrese un numero para verificar si es par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

print("\n---------------------------Ejercicio 4---------------------------\n")
    
""" 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años. """

edad : int = int(input("Ingrese su edad para determinar su categoria: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolecente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

print("\n---------------------------Ejercicio 5---------------------------\n")
    
""" 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string. """

contraseña : str = str(input("Ingrese una contraseña que contenga entre 8 y 14 caracteres: "))
longitud_de_contraseña = len(contraseña)

if longitud_de_contraseña >= 8 and longitud_de_contraseña <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
 
print("\n---------------------------Ejercicio 6---------------------------\n")
   
""" 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. """

from statistics import mode, median, mean
import random
listita = [random.randint(1, 100) for i in range(50)]
print(listita)

moda = mode(listita)
mediana = median(listita)
media = mean(listita)

if (media > mediana) and (mediana > moda):
    print("Sesgo positivo o a la derecha")
elif (media < mediana) and (mediana < moda):
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

print("\n---------------------------Ejercicio 7---------------------------\n")
    
""" 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla. """

palabra : str = str(input("Ingrese una palabra: "))
ultima_letra = palabra[-1]
vocales = ["a", "e", "i", "o", "u"]

if ultima_letra.lower() in vocales:
    palabra = palabra + "!"
    print(palabra)
else:
    print(palabra)
    

print("\n---------------------------Ejercicio 8---------------------------\n")

""" 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas. """

nombre : str = str(input("Ingrese su nombre: "))
print(f"Hola {nombre}! que te gustaria hacer? \n 1) Quiero ver mi nombre en MAYUSCULAS \n 2) Quiero ver mi nombre en minusculas \n 3) Quiiero ver mi nombre solo con la primer letra en Mayuscula")
opcion : int = int(input("\nIngresa la opcion que deseas 1, 2 o 3: "))

if opcion == 1:
    nombre = nombre.upper()
    print(nombre)
elif opcion == 2:
    nombre = nombre.lower()
    print(nombre)
elif opcion == 3:
    nombre = nombre.capitalize()
    print(nombre)
else:
    print("opcion no valida")

print("\n---------------------------Ejercicio 9---------------------------\n")
    
""" 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). """

magnitud = float(input("Ingresa la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")


print("\n---------------------------Ejercicio 10---------------------------\n")
    
""" 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano. """

print("En cual hemisferio te encuentras? \n 1) Norte \n 2) Sur")
hemisferio : int = int(input("Por favor elige tu emisferio (ingresa 1 o 2) "))

print("Selecciona tu mes:\n"
      "1) Enero\n"
      "2) Febrero\n"
      "3) Marzo\n"
      "4) Abril\n"
      "5) Mayo\n"
      "6) Junio\n"
      "7) Julio\n"
      "8) Agosto\n"
      "9) Septiembre\n"
      "10) Octubre\n"
      "11) Noviembre\n"
      "12) Diciembre")

mes = int(input("Ingresa el número de tu mes: "))

dia : int = int(input("Ingresa el numero del dia del mes: "))

if hemisferio == 1:
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Estas en invierno")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Estas en Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <=20):
        print("Estas en Verano")
    elif (mes == 6 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Estas en Otoño")
elif hemisferio == 2:
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Estas en Verano")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Estas en Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <=20):
        print("Estas en Invierno")
    elif (mes == 6 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Estas en Primavera")
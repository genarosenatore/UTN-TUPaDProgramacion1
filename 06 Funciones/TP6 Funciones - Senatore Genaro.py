#TP6 FUNCIONES - SENATORE GENARO

"""1) Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""

print("--------------------------------------EJERCICIO N1--------------------------------------")

def imprimir_hola_mundo():
    print("Hola mundo")

imprimir_hola_mundo()

"""2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""

print("--------------------------------------EJERCICIO N2--------------------------------------")
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Ingresa tu nombre")
saludar_usuario(nombre)

"""3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados."""

print("--------------------------------------EJERCICIO N3--------------------------------------")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}. tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
edad = input("Ingrese la edad: ")
residencia = input("Ingrese la residencia: ")

informacion_personal(nombre,apellido,edad,residencia)

"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y 
devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados."""

print("--------------------------------------EJERCICIO N4--------------------------------------")

def calcular_area_circulo(radio:float):
    area : float = 3.14 * (radio*radio)
    return area
    
def calcular_perimetro_circulo(radio:float):
    perimetro : float = 2 * 3.14 * radio
    return perimetro

radio = float(input ("Ingrese el radio: "))
print(f"el area del circulo es {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es {calcular_perimetro_circulo(radio)}")


"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""
print("--------------------------------------EJERCICIO N5--------------------------------------")

def segundos_a_horas(segundos):
    horas : float = (segundos/60)/60
    return horas

segundos:float = float(input("Ingrese una cantidad de segundos: "))
print(segundos_a_horas(segundos))

"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""

print("--------------------------------------EJERCICIO N6--------------------------------------")

def tabla_multiplicar(numero: int):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)

"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara."""

print("--------------------------------------EJERCICIO N7--------------------------------------")
def operaciones_basicas(a: float, b: float):
    return (a + b, a - b, a * b, a / b)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número (distinto de 0): "))

suma, resta, mult, div = operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {mult}")
print(f"División: {div}")

"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""
print("--------------------------------------EJERCICIO N8--------------------------------------")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros (ej: 1.75): "))

imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""
print("--------------------------------------EJERCICIO N9--------------------------------------")

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en °C: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F")

"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función."""
print("--------------------------------------EJERCICIO N10--------------------------------------")

def calcular_promedio(a, b, c):
    return (a+b+c)/3

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio es: {promedio:.2f}")

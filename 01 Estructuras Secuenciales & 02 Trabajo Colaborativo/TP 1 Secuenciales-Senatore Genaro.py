# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print ("Hola mundo!")
 

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
Nombre = input("Ingresa tu nombre ")
print(f"Hola {Nombre}! un placer conocerte.")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

Nombre = input("Ingresa tu nombre: ")
Apellido = input("Ingresa tu apellido: ")
Edad = input("Ingresa tu edad: ")

print(f"Soy {Nombre} {Apellido}, tengo {Edad} años y vivo en Argentina")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

Radio = float(input("Ingrese Radio del circulo para conocer su Area y Perimetro -> "))
pi = 3.14
Area = pi*(Radio**2)
Perimetro = 2*pi*Radio
print(f"El Area del circulo es {Area:.2f}m2 y su perimetro es {Perimetro}m")


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

Segundos = int(input("Ingresa la cantidad de segundos que quieras y te digo a cuantas horas equivale :) "))
Minutos = Segundos/60
Horas = Minutos/60
print(f"Los {Segundos} segundos equivalen a {Horas:.2f} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

Numero = int(input("Ingrese un numero para ver su tabla de multiplicar -> "))
for i in range (10):
    print(f"{Numero}*{i+1} = {Numero*(i+1)}")
    
#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

Numero_uno = int(input("Ingrese un numero entero distinto de 0 "))
Numero_dos= int(input("Ingrese otro numero entero distinto de 0"))

suma = Numero_uno+Numero_dos
division = Numero_uno/Numero_dos
multipicacion = Numero_uno*Numero_dos
resta = Numero_uno-Numero_dos

print(f""" 
      
      La suma es {suma}
      La division es {division}
      La multiplicacion es {multipicacion}
      La resta es {resta}3
      
      """)

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. 

Altura = int(input("ingrese su altura en centimetros "))
Peso = float(input("ingrese su peso en kg "))
Altura_en_metros = Altura/100

IMC = float(Peso/Altura_en_metros**2)

print(f"Su indice de masa corporal es de {IMC:.2f}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit.

tempC = float(input("ingrese la temperatura en grados celsius -> "))
tempF = float((1.8*tempC + 32))

print(f"la temperatura en farenheit es: {tempF:.2f}F")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

Num1 = float(input("Ingrese un numero -> "))
Num2 = float(input("Ingrese un numero -> "))
Num3 = float(input("Ingrese un numero -> "))

promedio= float((Num1+Num2+Num3)/3)
print(f"El promedio de los numeros ingresados es: {promedio:.2f}")
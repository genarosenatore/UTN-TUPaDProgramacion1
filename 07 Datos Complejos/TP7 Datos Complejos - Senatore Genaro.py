#TP7 DATOS COMPLEJOS - SENATORE GENARO
"""1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300"""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

"""2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:"""

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

"""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""
mi_lista= list(precios_frutas.keys())

"""4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""

contactos = {}

print("A continuacion debera cargar sus primeros 5 contactos:")
for i in range (1,6):
    print(f"Cargue el contacto nro{i}")
    nombre : str = str(input("Ingrese el nombre: ")).strip().capitalize()
    numero : str = str(input("Ingrese el numero: ")).strip()
    contactos[nombre] = numero

buscado: str = input("¿A quién querés buscar? ").strip().title()
numero = contactos.get(buscado)

if numero is not None:
    print(f"{buscado}: {numero}")
else:
    print("No existe un contacto con ese nombre.")
    
"""5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra."""

frase = input("Ingrese una frase: ").lower()
palabras = frase.split()             


palabras_unicas = set(palabras)
print(palabras)

frecuencias = {}
for p in palabras:
    if p in frecuencias:
        frecuencias[p] += 1
    else:
        frecuencias[p] = 1

print("Palabras únicas:", palabras_unicas)
print("Frecuencia:", frecuencias)

"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno."""

alumnos = {}

for i in range (1,4):
    nombre : str = str(input(f"Ingrese el nombre del alumno N{i}: ")).strip().title()
    notas=tuple(float(input(f"Nota {j}: ")) for j in range(1, 4))
    alumnos[nombre] = notas
    
print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"- {nombre}: {promedio:.2f} (notas: {notas})")
    
"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {1, 5, 6, 7}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2  
al_menos_uno = parcial1 | parcial2

print("Ambos:", sorted(ambos))
print("Solo uno:", sorted(solo_uno))
print("Al menos uno:", sorted(al_menos_uno))

    
"""8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe."""

productos = {
    'ventilador': 5,
    'climatizador': 6,
    'aire': 10,
}

while True:
    print("\nMenú:")
    print("1) Consultar stock")
    print("2) Agregar unidades a un producto existente")
    print("3) Agregar producto nuevo")
    print("4) Listar productos")
    print("0) Salir")
    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        nombre = input("Producto a consultar: ").strip().lower()
        if nombre in productos:
            print(f"Stock de '{nombre}': {productos[nombre]}")
        else:
            print("Ese producto no existe.")

    elif opcion == "2":
        nombre = input("Producto al que querés sumar stock: ").strip().lower()
        if nombre in productos:
            unidades = int(input("¿Cuántas unidades sumás? "))  # asumimos entero válido
            productos[nombre] += unidades
            print(f"Nuevo stock de '{nombre}': {productos[nombre]}")
        else:
            print("No existe. Usá la opción 3 para agregarlo.")

    elif opcion == "3":
        nombre = input("Nombre del nuevo producto: ").strip().lower()
        if nombre in productos:
            print("Ya existe. Usá la opción 2 para sumar stock.")
        else:
            unidades = int(input("Stock inicial: "))  # asumimos entero válido
            productos[nombre] = unidades
            print(f"Agregado '{nombre}' con stock {unidades}.")

    elif opcion == "4":
        if not productos:
            print("No hay productos cargados.")
        else:
            for p, s in productos.items():
                print(f"- {p}: {s}")

    elif opcion == "0":
        break

    else:
        print("Opción inválida.")
        
"""9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora."""

agenda = {
    ("lunes" , "10:00"): "Reunion",
    ("martes", "15:00"): "Clase de ingles"
}

dia = input("Día: ").strip().lower()     
hora = input("Hora (Hora:Minutos) ej -> 18:00: ").strip()   

evento = agenda.get((dia, hora))
if evento:
    print(f"En {dia} a las {hora}: {evento}")
else:
    print("No hay actividad en ese día y hora.")
    
    
"""10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}

for k,v in original.items():
    invertido[v] = k

print(original)
print(invertido)
"""1. Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad"""

productos = [
    "banana, 2000, 20\n",
    "manzana, 2500, 10\n",
    "naranja, 1800, 15\n"
]

with open("productos.txt", "w") as archivo:
    archivo.writelines(productos)
    
"""2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato: 
Producto: Lapicera | Precio: $120.5 | Cantidad: 30
"""

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = [p.strip() for p in linea.split(",")]
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
        
"""3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente."""

flag = True
while flag:
    print("Ingrese un nuevo producto:")
    n : str = str(input("Ingrese el nombre del producto: "))
    p : str = str(input("Ingrese el precio del producto: $"))
    c : str = str(input("Ingrese la cantidad del producto: "))

    nuevo_producto = f"{n},{p},{c}\n"

    with open("productos.txt", "a") as archivo:
        archivo.write(nuevo_producto)
    
    opcion : int = int(input("Queres ingresar mas productos? 1.SI / 2.NO"))
    if opcion == 2:
        flag = False
    else:
        flag = True
    
"""4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad."""

lista_dict_productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = [p.strip() for p in linea.split(",")]
        lista_dict_productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

"""5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error."""

buscado = input("Ingrese el nombre del producto a buscar: ").strip().lower()

encontrado = None
for p in lista_dict_productos:
    if p["nombre"].strip().lower() == buscado:
        encontrado = p
        break
if encontrado:
    print(f"Producto: {encontrado['nombre']} | Precio: ${encontrado['precio']} | Cantidad: {encontrado['cantidad']}")
else:
    print("No se encontró el producto.")
    
"""6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista"""

with open("productos.txt", "w") as archivo:
    for p in lista_dict_productos:
        archivo.write(f'{p["nombre"]},{p["precio"]},{p["cantidad"]}\n')

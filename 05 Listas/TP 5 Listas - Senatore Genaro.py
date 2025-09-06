# TP 5 LISTAS - SENATORE GENARO

"""1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range."""
print("--------------------------------------EJERCICIO N1--------------------------------------")
lista_numeros : list = []
for i in range(1,101):
    if i%4 == 0:
        lista_numeros.append(i)

print(lista_numeros)


"""2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!"""
print("--------------------------------------EJERCICIO N2--------------------------------------")
mi_lista : list = [3,33,333,3333,33333]
print(mi_lista[-2])

"""3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
ejemplo:
lista_vacia = []"""
print("--------------------------------------EJERCICIO N3--------------------------------------")
mi_lista_vacia : list = []
mi_lista_vacia.append("palabra1")
mi_lista_vacia.append("palabra2")
mi_lista_vacia.append("palabra3")
print(mi_lista_vacia)

"""4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]"""
print("--------------------------------------EJERCICIO N4--------------------------------------")
animales : list = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)
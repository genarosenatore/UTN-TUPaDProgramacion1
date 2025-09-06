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

"""5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza."""
print("--------------------------------------EJERCICIO N5--------------------------------------")
numeros : list = [8, 15, 3, 22, 7] #CREAMOS LA LISTA DE NUMEROS
numeros.remove(max(numeros)) #TOMAMOS EL VALOR MAS GRANDE DE LA LISTA Y LO ELIMINAMOS
print(numeros) #MOSTRAMOS LA NUEVA LISTA SIN EL NUMERO 22 EL CUAL FUE REMOVIDO PORQUE ERA EL MAS GRANDE DE LA LISTA ANTERIOR

"""6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros."""
print("--------------------------------------EJERCICIO N6--------------------------------------")
lista_del_10_al_30_con_saltos_de_5 : list = []
for i in range(10,31,5):
        lista_del_10_al_30_con_saltos_de_5.append(i)
print(lista_del_10_al_30_con_saltos_de_5)

"""7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
"""
print("--------------------------------------EJERCICIO N7--------------------------------------")
autos : list = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["sirocco", "rcz"]
print(autos)

"""8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla."""
print("--------------------------------------EJERCICIO N8--------------------------------------")
dobles : list = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

"""9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla
"""
print("--------------------------------------EJERCICIO N9--------------------------------------")
compras : list= [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo") #punto a
compras[1][1]="tallarines" #punto b
compras[0].remove("pan") #punto c
print(compras) #punto d
"""10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla.

"""
print("--------------------------------------EJERCICIO N10--------------------------------------")
lista_anidada : list = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)

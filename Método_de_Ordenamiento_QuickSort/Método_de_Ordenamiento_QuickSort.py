# Lista desordenada que se desea ordenar
datos = [20, 2, 15, 16, 8, 1, 7, 11, 3, 9, 4, 5, 10, 6, 12, 14, 19, 13, 17, 19, 18]

# Función para dividir la lista en dos partes con base en un pivote
def dividir(lista):
    # Elegir un pivote, en este caso, el primer elemento
    pivote = lista[0]

    # Crear listas para los elementos menores y mayores que el pivote
    izquierda = []
    derecha = []

    # Recorremos los elementos de la lista, excluyendo el primero (pivote)
    for elemento in lista[1:]:
        if elemento < pivote:
            izquierda.append(elemento)
        else:
            derecha.append(elemento)
    
    # Imprimir cómo se ha dividido la lista
    print(f"División de la lista: {lista}")
    print(f"Menores: {izquierda}, Pivote: {pivote}, Mayores: {derecha}")
    
    # Retornar las sublistas y el pivote
    return izquierda, pivote, derecha

# Función para ordenar la lista usando QuickSort
def ordenar(lista):
    # Caso base: si la lista tiene un solo elemento o está vacía, no se necesita ordenar
    if len(lista) <= 1:
        return lista

    # Dividir la lista en sublistas
    izquierda, pivote, derecha = dividir(lista)

    # Recursión: ordenar las sublistas y luego unirlas con el pivote en el medio
    lista_ordenada = ordenar(izquierda) + [pivote] + ordenar(derecha)

    # Mostrar el progreso de la lista ordenada
    print(f"Combinando: {lista_ordenada}")
    return lista_ordenada

# Ordenar la lista y mostrar el resultado
print("\nResultado final ordenado:", ordenar(datos))

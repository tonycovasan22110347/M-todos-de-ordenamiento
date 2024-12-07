# Lista desordenada que se desea ordenar
lista = [6, 8, 2, 3, 1, 9, 4, 7, 5]

# Imprimir la lista inicial
print("Lista inicial:", lista)

# Iteración principal para ordenar la lista
for i in range(len(lista)):
    # Tomar el valor actual que será insertado en la sublista ordenada
    valor_a_insertar = lista[i]
    # Iniciar el índice en la posición actual
    j = i

    # Mostrar información sobre la iteración
    print(f"\nIteración {i + 1}:")
    print(f"Valor a insertar: {valor_a_insertar}")

    # Mover el valor actual a su posición correcta
    while j > 0 and lista[j - 1] > valor_a_insertar:
        # Mostrar la comparación
        print(f"Comparando {lista[j - 1]} > {valor_a_insertar}: True")

        # Desplazar el elemento hacia la derecha
        lista[j] = lista[j - 1]
        j -= 1  # Mover el índice a la izquierda

        # Mostrar el estado de la lista
        print("Lista actualizada:", lista)

    # Insertar el valor en la posición correcta
    lista[j] = valor_a_insertar

    # Mostrar el resultado de la inserción
    print(f"Insertado {valor_a_insertar} en la posición {j}")
    print("Estado de la lista:", lista)

# Mostrar la lista final después de ordenar
print("\nLista ordenada:", lista)

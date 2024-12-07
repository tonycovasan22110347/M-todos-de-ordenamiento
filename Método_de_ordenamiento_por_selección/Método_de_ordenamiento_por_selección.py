# Lista desordenada que será ordenada de menor a mayor.
numeros = [6, 8, 2, 3, 1, 9, 4, 7, 5]

# Se obtiene el tamaño de la lista para establecer los límites del ciclo.
n = len(numeros)

# Ciclo externo para recorrer los elementos de la lista.
for index in range(n - 1):
    # Mostrar el estado de la lista en cada iteración del ciclo externo.
    print(f"\nEstado de la lista: {numeros}")
    
    # Inicialización de la posición del menor elemento encontrado.
    indice_menor = index
    print(f"Comenzando con el índice {index}, donde el valor actual es {numeros[index]}")

    # Ciclo interno para encontrar el valor más pequeño en el resto de la lista.
    for comparador in range(index + 1, n):
        # Compara los valores y actualiza el índice del menor valor si es necesario.
        if numeros[comparador] < numeros[indice_menor]:
            indice_menor = comparador
            print(f"Se encuentra un valor menor: {numeros[indice_menor]} en la posición {indice_menor}")
    
    # Realiza el intercambio si el menor no está en la posición actual.
    if indice_menor != index:
        print(f"Intercambiando {numeros[index]} con {numeros[indice_menor]}")
        numeros[index], numeros[indice_menor] = numeros[indice_menor], numeros[index]
    else:
        print("No se necesita hacer intercambio en esta iteración.")
    
# Muestra el resultado final de la lista ordenada.
print("\nLista ordenada:", numeros)

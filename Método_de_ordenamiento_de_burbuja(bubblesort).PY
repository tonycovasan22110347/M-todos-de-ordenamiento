# Lista de números que vamos a ordenar
numeros = [5, 8, 7, 9, 3, 2, 1, 6, 4]

# Bucle principal para realizar múltiples pasadas sobre la lista
for i in range(len(numeros) - 1):  # Iteración para recorrer la lista completa
    for j in range(len(numeros) - 1):  # Comparación de elementos adyacentes
        print(f"Comparando: {numeros[j]} con: {numeros[j + 1]}")
        
        # Si el elemento actual es mayor que el siguiente, los intercambiamos
        if numeros[j] > numeros[j + 1]:
            # Intercambio de los dos elementos
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
            
            # Mostrar el intercambio realizado
            print(f"Intercambiando: {numeros[j]} con: {numeros[j + 1]}")

print(f"Lista ordenada final: {numeros}")

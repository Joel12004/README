# Definición de la matriz bidimensional de 3x3
matriz = [
    [9, 3, 6],
    [7, 5, 1],
    [4, 8, 2]
]


# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)


# Función para ordenar una fila específica de la matriz usando Bubble Sort
def ordenar_fila(matriz, fila_index):
    fila = matriz[fila_index]

    # Implementación de Bubble Sort para ordenar la fila
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                # Intercambiar elementos
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

    # Asignar la fila ordenada de vuelta a la matriz
    matriz[fila_index] = fila


# Mostrar la matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Ordenar la fila 1 (segunda fila) de la matriz
fila_a_ordenar = 1
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz después de ordenar la fila
print("\nMatriz después de ordenar la fila 1:")
imprimir_matriz(matriz)

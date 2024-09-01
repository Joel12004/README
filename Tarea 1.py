# Definición de la matriz bidimensional de 3x3
matriz = [
    [5, 8, 3],
    [6, 1, 9],
    [7, 2, 4]
]

# Función para buscar un valor en la matriz
def buscar_valor_en_matriz(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return (i, j)  # Retorna la posición (fila, columna)
    return None  # Si no se encuentra el valor, retorna None

# Valor a buscar en la matriz
valor_buscado = 9

# Búsqueda del valor en la matriz
resultado = buscar_valor_en_matriz(matriz, valor_buscado)

# Mostrar resultado
if resultado is not None:
    print(f"El valor {valor_buscado} se encontró en la posición (fila, columna): {resultado}")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")

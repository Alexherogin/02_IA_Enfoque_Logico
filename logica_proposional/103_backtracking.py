#bracktracking

def es_seguro(tablero, fila, columna, N):
    # Verifica si es seguro colocar una reina en la fila y columna dadas
    # Verifica la columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False

    # Verifica la diagonal izquierda superior
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Verifica la diagonal derecha superior
    for i, j in zip(range(fila, -1, -1), range(columna, N)):
        if tablero[i][j] == 1:
            return False

    return True

def resolver_n_reinas(tablero, fila, N):
    # Función recursiva para colocar las reinas en el tablero
    if fila == N:
        # Todas las reinas se han colocado con éxito
        return True

    for columna in range(N):
        if es_seguro(tablero, fila, columna, N):
            tablero[fila][columna] = 1  # Coloca la reina en la posición segura
            if resolver_n_reinas(tablero, fila + 1, N):  # Llama recursivamente para la siguiente fila
                return True
            tablero[fila][columna] = 0  # Si no se puede colocar la reina, retrocede y prueba otra columna

    return False  # Si no se puede colocar la reina en ninguna columna de esta fila, devuelve False

def imprimir_tablero(tablero):
    # Imprime el tablero de ajedrez con las reinas colocadas
    N = len(tablero)
    for i in range(N):
        for j in range(N):
            print(tablero[i][j], end=" ")
        print()

def n_reinas(N):
    # Función principal para encontrar la solución al problema de las N reinas
    tablero = [[0] * N for _ in range(N)]  # Crea un tablero vacío NxN
    if resolver_n_reinas(tablero, 0, N):  # Intenta colocar las reinas en el tablero
        print(f"Solución para {N} reinas:")
        imprimir_tablero(tablero)  # Si se encuentra una solución, imprime el tablero
    else:
        print(f"No hay solución para {N} reinas.")  # Si no se encuentra una solución, muestra un mensaje

if __name__ == "__main__":
    # Se ejecuta cuando el script se ejecuta directamente
    N = 8  # Número de reinas
    n_reinas(N)  # Encuentra la solución para el problema de las N reinas

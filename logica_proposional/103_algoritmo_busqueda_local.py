

import random

def funcion_objetivo(x):
    # Función objetivo a maximizar (en este caso, un simple polinomio cuadrático)
    return -x**2 + 10*x + 5

def generar_vecino(actual, paso):
    # Genera un vecino aleatorio dentro de un cierto paso de distancia del valor actual
    return actual + random.uniform(-paso, paso)

def ascenso_colinas(paso, intentos):
    # Algoritmo de ascenso de colinas para encontrar el máximo de la función objetivo
    mejor_valor = float('-inf')  # Mejor valor encontrado hasta el momento (inicializado como negativo infinito)
    mejor_solucion = None  # Mejor solución encontrada hasta el momento
    # Realizamos varios intentos para encontrar el máximo
    for _ in range(intentos):
        solucion_actual = random.uniform(-10, 10)  # Genera una solución inicial aleatoria en el rango [-10, 10]
        valor_actual = funcion_objetivo(solucion_actual)  # Calcula el valor de la función objetivo para la solución actual
        # Bucle principal del algoritmo de ascenso de colinas
        while True:
            vecino = generar_vecino(solucion_actual, paso)  # Genera un vecino aleatorio dentro del paso especificado
            valor_vecino = funcion_objetivo(vecino)  # Calcula el valor de la función objetivo para el vecino
            if valor_vecino > valor_actual:  # Si el vecino tiene un valor mayor, actualiza la solución actual
                solucion_actual = vecino
                valor_actual = valor_vecino
            else:  # Si no, termina el bucle y pasa al siguiente intento
                break
        # Actualiza la mejor solución y valor encontrados hasta el momento si se encuentra uno mejor en este intento
        if valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_solucion = solucion_actual
    # Devuelve la mejor solución y valor encontrados en todos los intentos
    return mejor_solucion, mejor_valor

if __name__ == "__main__":
    paso = 0.1  # Tamaño del paso para generar vecinos
    intentos = 100  # Número de intentos para buscar el máximo
    mejor_solucion, mejor_valor = ascenso_colinas(paso, intentos)
    print(f"Mejor solución encontrada: {mejor_solucion}, con valor: {mejor_valor}")

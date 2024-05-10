
# cuantificadores


# Definimos un dominio de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Expresión cuantificada: Para todo x en el dominio, existe un y en el dominio tal que y es mayor que x
resultado = all(any(y > x for y in numeros) for x in numeros)

if resultado:
    print("La expresión es verdadera para todos los números en el dominio.")
else:
    print("La expresión no es verdadera para todos los números en el dominio.")

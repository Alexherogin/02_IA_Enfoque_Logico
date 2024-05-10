

def unificar(termino1, termino2, sustitucion={}):
    if termino1 == termino2:
        return sustitucion
    elif isinstance(termino1, str) and termino1.islower():
        return unificar_variable(termino1, termino2, sustitucion)
    elif isinstance(termino2, str) and termino2.islower():
        return unificar_variable(termino2, termino1, sustitucion)
    elif isinstance(termino1, list) and isinstance(termino2, list) and len(termino1) == len(termino2):
        for t1, t2 in zip(termino1, termino2):
            sustitucion = unificar(t1, t2, sustitucion)
        return sustitucion
    else:
        return None

def unificar_variable(variable, termino, sustitucion):
    if variable in sustitucion:
        return unificar(sustitucion[variable], termino, sustitucion)
    elif termino in sustitucion:
        return unificar(variable, sustitucion[termino], sustitucion)
    else:
        sustitucion[variable] = termino
        return sustitucion

# Ejemplo de unificación exitosa
expresion1 = ["padre", "X", "Y"]
expresion2 = ["padre", "Juan", "Maria"]

sustitucion = unificar(expresion1, expresion2)

if sustitucion is not None:
    print("Unificación exitosa. Sustitución:")
    for key, value in sustitucion.items():
        print(f"{key} = {value}")
else:
    print("No se puede unificar las expresiones.")

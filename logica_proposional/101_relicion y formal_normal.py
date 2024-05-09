

def clausula_vacia(clausula):
    """Verifica si una cláusula es la cláusula vacía."""
    return len(clausula) == 0

def resolvente(clausula1, clausula2, literal):
    """Calcula la resolvente de dos cláusulas respecto a un literal."""
    nueva_clausula = (clausula1 - {literal}) | (clausula2 - {negacion(literal)})
    return nueva_clausula

def negacion(literal):
    """Devuelve la negación de un literal."""
    if literal.startswith("~"):
        return literal[1:]
    else:
        return "~" + literal

def resolucion_proposicional(clausulas):
    """Realiza la resolución proposicional hasta que no se puedan obtener más resolventes."""
    while True:
        nuevas_clausulas = set()
        for clausula1 in clausulas:
            for clausula2 in clausulas:
                if clausula1 != clausula2:
                    for literal in clausula1:
                        if negacion(literal) in clausula2:
                            nueva_clausula = resolvente(clausula1, clausula2, literal)
                            if clausula_vacia(nueva_clausula):
                                return True  # Se encontró una contradicción, la fórmula es válida
                            nuevas_clausulas.add(nueva_clausula)
        if nuevas_clausulas.issubset(clausulas):
            return False  # No se pueden obtener más resolventes, la fórmula no es válida
        clausulas.update(nuevas_clausulas)

# Ejemplo de uso
clausula1 = {"p", "~q"}
clausula2 = {"~p", "r"}
clausula3 = {"q", "~r"}
clausulas = {clausula1, clausula2, clausula3}

if resolucion_proposicional(clausulas):
    print("La fórmula es válida.")
else:
    print("La fórmula no es válida.")







# Definimos las funciones de Skolem
def skolem(x):
    return f"Profesor({x})"

# Premisas originales
premisas = [
    "forall x: Estudiante(x) -> Profesor(pedro(x))",
    "Estudiante(Juan)"
]

# Aplicamos la resolución de Skolem
nuevas_premisas = []
for premisa in premisas:
    if "forall" in premisa:
        # Obtenemos la variable cuantificada existencialmente
        variable = premisa.split(":")[1].split(" ")[1]
        # Reemplazamos la cuantificación existencial por la función de Skolem
        nueva_premisa = premisa.replace(f"skolem({variable})", skolem(variable))
        nuevas_premisas.append(nueva_premisa)
    else:
        nuevas_premisas.append(premisa)

# Mostramos las premisas resultantes
for premisa in nuevas_premisas:
    print(premisa)

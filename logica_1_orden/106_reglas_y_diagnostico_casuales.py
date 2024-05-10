# Definición de reglas diagnósticas: cada regla relaciona síntomas con posibles causas
reglas_diagnosticas = {
    "Regla 1": {"Síntoma A": "Causa X"},
    "Regla 2": {"Síntoma B": "Causa Y"},
    "Regla 3": {"Síntoma A": "Causa Z", "Síntoma B": "Causa Y"},
    "Regla 4": {"Síntoma C": "Causa X"}
}

# Función para realizar el diagnóstico de las posibles causas dado un conjunto de síntomas
def diagnosticar_sintomas(sintomas, reglas):
    causas_posibles = set()  # Creamos un conjunto para almacenar las posibles causas

    # Iteramos sobre las reglas
    for regla, causas in reglas.items():
        # Comparamos los síntomas observados con los síntomas de cada regla
        sintomas_coincidentes = set(sintomas) & set(causas.keys())
        # Si los síntomas observados coinciden con los síntomas de la regla
        if sintomas_coincidentes == set(causas.keys()):
            # Agregamos las posibles causas de esta regla al conjunto de causas posibles
            causas_posibles.update(set(causas.values()))

    return causas_posibles  # Devolvemos las posibles causas identificadas

# Síntomas observados
sintomas_observados = ["Síntoma A", "Síntoma C"]

# Realizar el diagnóstico
causas_posibles = diagnosticar_sintomas(sintomas_observados, reglas_diagnosticas)

# Mostrar el resultado del diagnóstico
if causas_posibles:
    print("Posibles causas identificadas:", causas_posibles)
else:
    print("No se pudo identificar una causa con los síntomas observados.")

#La función diagnosticar_sintomas recibe
# los síntomas observados y las reglas diagnósticas,
# y devuelve un conjunto de posibles causas identificadas.
# Finalmente, se muestra el resultado del diagnóstico.







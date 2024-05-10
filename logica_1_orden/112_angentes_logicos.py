class AgenteLogico:
    def __init__(self, nombre, reglas_decision):
        self.nombre = nombre  # Nombre del agente
        self.reglas_decision = reglas_decision  # Reglas de decisión del agente

    def tomar_decision(self, informacion):
        for regla, decision in self.reglas_decision.items():  # Itera sobre las reglas de decisión
            if regla in informacion and informacion[regla]:  # Verifica si la regla está en la información y es verdadera
                return decision  # Devuelve la decisión asociada a la regla que se cumple
        return "Sin decisión"  # Si ninguna regla se cumple, devuelve un mensaje de "Sin decisión"

# Crear un agente lógico con reglas de decisión
reglas_decision = {
    "informacion_importante": "Tomar acción A",
    "informacion_secundaria": "Tomar acción B"
}
agente = AgenteLogico("Agente1", reglas_decision)  # Crea una instancia de AgenteLogico

# Simular una situación con información
informacion = {"informacion_importante": True}  # Define la información relevante para la decisión

# El agente toma una decisión en función de la información
decision = agente.tomar_decision(informacion)  # Llama al método tomar_decision del agente

# Imprime la decisión tomada por el agente
print(f"{agente.nombre} decide: {decision}")  # Muestra la decisión tomada por el agente en función de la información proporcionada

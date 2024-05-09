
# Base de conocimientos en lógica proposicional
base_conocimientos = {
    'hechos': {
        'llueve': True,   # Hecho: Es un día lluvioso
        'nieva': True,    # Hecho: Es un día nevado
    },
    'reglas': {
        'clima_frio': lambda bc: bc['hechos']['nieva'],   # Regla: Si nieva, entonces hace frío
    }
}

# Consulta a la base de conocimientos
def consultar_base_conocimiento(base_conocimientos):
    try:
        # Se evalúa la regla "clima_frio" utilizando la función lambda definida en la base de conocimientos
        clima_frio = base_conocimientos['reglas']['clima_frio'](base_conocimientos)
        return clima_frio
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Se consulta la base de conocimientos para determinar si hace frío o no
    clima_frio = consultar_base_conocimiento(base_conocimientos)
    if clima_frio:
        print("Hace frío.")
    else:
        print("No hace frío.")

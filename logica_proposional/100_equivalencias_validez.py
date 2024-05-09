
# equivalencas y valides

from sympy import symbols, Implies, satisfiable, ask

# Definimos las variables simbólicas
p, q, r = symbols('p q r')

# Definimos dos expresiones lógicas en español
expresion1 = Implies(p, q)  # Implicación: Si p, entonces q
expresion2 = Implies(q, r)  # Implicación: Si q, entonces r

# Verificamos si la primera expresión implica la segunda
if ask(Implies(expresion1, expresion2), True):
    print("La primera expresión implica la segunda.")
else:
    print("La primera expresión no implica la segunda.")

# Verificamos si la segunda expresión implica la primera
if ask(Implies(expresion2, expresion1), True):
    print("La segunda expresión implica la primera.")
else:
    print("La segunda expresión no implica la primera.")

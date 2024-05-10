
from pyswip import Prolog

# Crear una instancia de Prolog
prolog = Prolog()

# Definir hechos
prolog.assertz("padre(juan, pedro)")
prolog.assertz("padre(pedro, ana)")
prolog.assertz("mujer(maria)")
prolog.assertz("mujer(ana)")

# Definir reglas
prolog.assertz("abuelo(X, Y) :- padre(X, Z), padre(Z, Y)")
prolog.assertz("abuelo(X, Y) :- padre(X, Z), mujer(Z), madre(Z, Y)")
prolog.assertz("madre(X, Y) :- padre(Y, X), mujer(X)")

# Consulta
for solucion in prolog.query("abuelo(juan, X)"):
    print(solucion["X"], "es el abuelo de alguien")

# Consulta
for solucion in prolog.query("abuelo(juan, ana)"):
    print(solucion["X"], "es abuelo de ana")

# Consulta
for solucion in prolog.query("madre(X, Y)"):
    print(solucion["X"], "es madre de", solucion["Y"])
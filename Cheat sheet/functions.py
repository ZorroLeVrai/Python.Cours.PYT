"""
Les fonctions
"""
from collections.abc import Callable

#fonction qui ne prend aucun paramètre
def do_nothing():
    pass

#fonction avec plusieurs paramètres
def imprimer_somme(op1: float, op2: float) -> None:
    print(op1 + op2)

#fonction avec plusieurs paramètres et une valeur de retour
def somme(op1: float, op2: float) -> float:
    return op1 + op2

"""
Les fonctions lambda
"""

# fonction lambda avec un argument
incrementer = lambda x: x+1
# print(incrementer(5))   #6

# fonction lambda avec zero argument
obtenir_zero = lambda : 0
# print(obtenir_zero())   #0

# fonction lambda avec 2 arguments
additionner = lambda a,b: a + b
# print(additionner(1,2)) #3

"""
Les fonctions récursives
"""

#fonction recursive
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Le paramètre n doit être supérieur ou égal à zéro")
    if n == 0:
        return 1
    return n * factorial(n-1)

"""
Les fonctions locales
"""
def imprimer_factorial(n: int) -> None:
    def imprimer(valeur: int) -> None:
        print(f"Factoriel de {n} = {valeur}")

    resultat = factorial(n)
    imprimer(resultat)

# imprimer_factorial(5)  #120

"""
Fonction prenant d'autres fonctions en paramètre
"""
def calculer_imprimer(calculer: Callable[[], int], imprimer: Callable[[int], None]) -> None:
    resultat = calculer()
    imprimer(resultat)

# calculer_imprimer(lambda : factorial(5), lambda solution: print(f"Résultat {solution}"))    #Résultat 120

"""
Closures
"""
def illustrer_closure(nombre1: float, nombre2: float) -> None:
    calculer_v1 = lambda : nombre1 + nombre2
    def calculer_v2():
        return nombre1 + nombre2

    print(calculer_v1())
    print(calculer_v2())

illustrer_closure(5, 2);

def illustrer_closure_pb_reference():
    my_functions: list[Callable[[], None]] = list()

    for index in range(1, 9):
        my_functions.append(lambda: print(index))

    #execution des fonctions
    for func in my_functions:
        func()

# illustrer_closure_pb_reference()

def illustrer_resolution_pb_reference():
    def creer_fonction_imprimer(index: int) -> None:
        imprimer = lambda : print(index)
        return imprimer

    my_functions: list[Callable[[], None]] = list()

    for index in range(1, 9):
        my_functions.append(creer_fonction_imprimer(index))

    #execution des fonctions
    for func in my_functions:
        func()

# illustrer_resolution_pb_reference()

"""
Les fonctions generator
"""

# fonction generator
def ma_fonction_range(initial_value: int, max_value_excluded: int, step: int):
    current_value = initial_value
    while current_value < max_value_excluded:
        yield current_value
        current_value += step

# print(list(ma_fonction_range(1, 10, 2)))    #[1, 3, 5, 7, 9]

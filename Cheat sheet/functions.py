"""
Les fonctions
"""

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
print(incrementer(5))   #6

# fonction lambda avec zero argument
obtenir_zero = lambda : 0
print(obtenir_zero())   #0

# fonction lambda avec 2 arguments
additionner = lambda a,b: a + b
print(additionner(1,2)) #3

"""
Les fonctions récursives
"""

#fonction recursive
def factorial(n: int):
    if n < 0:
        raise ValueError("Le paramètre n doit être supérieur ou égal à zéro")
    if n == 0:
        return 1
    return n * factorial(n-1)

"""
Les fonctions generator
"""

# fonction generator
def ma_fonction_range(initial_value: int, max_value_excluded: int, step: int):
    current_value = initial_value
    while current_value < max_value_excluded:
        yield current_value
        current_value += step

print(list(ma_fonction_range(1, 10, 2)))    #[1, 3, 5, 7, 9]


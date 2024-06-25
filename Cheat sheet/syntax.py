"""
Les types de base
"""

# Types les plus utilisés en Python
var_int = 1             #type int
var_float = 3.14        #type float
var_string = "Bonjour"  #type str
var_bool = True         #type bool
var_none = None         #type NoneType

"""
Les opérateurs
"""

#opérations arithmétiques
print("Addition:", 1 + 2)                   #Addition: 3
print("Soustraction:", 2 - 1)               #Soustraction: 1
print("Multiplication:", 2 * 3)             #Multiplication: 6
print("Division flotante:", 3 / 2)          #Division flotante: 1.5
print("Division entière:", 3 // 2)          #Division entière: 1
print("Reste de division (modulo):", 4 % 3) #Reste de division (modulo): 1
print("Puissance:", 3**2)                   #Puissance: 9

#opérations booléennes
print("Opérateur ET:", True and True)       #Opérateur ET: True
print("Opérateur OU:", True or False)       #Opérateur OU: True
print("Opérateur de négation:", not False)  #Opérateur de négation: True

#opérations relationnels
print("Opérateur supérieur:", 4 > 3)            #Opérateur supérieur: True
print("Opérateur inférieur:", 4 < 3)            #Opérateur inférieur: False
print("Opérateur d'égalité:", 4 == 3)           #Opérateur d'égalité: False
print("Opérateur de non égalité:", 4 != 3)      #Opérateur de non égalité: True
print("Opérateur supérieur ou égal:", 4 >= 3)   #Opérateur supérieur ou égal: True
print("Opérateur inférieur ou égal:", 4 <= 3)   #Opérateur inférieur ou égal: False

"""
Les casts
"""

#opérations de casts
nombre_entier = int("45")
nombre_decimal = float("2.718")
boolean = bool(True)

"""
Les conditions
"""

nombre = 1
#la structure conditionnelle if
if nombre == 0:
    print("zéro")
elif nombre == 1:
    print("un")
else:
    print("autre")

#la structure conditionnelle match
match nombre:
    case 0:
        print("zéro")
    case 1:
        print("un")
    case _:
        print("autre")

#expression ternaire
resultat = "Zéro" if nombre == 0 else "Différent de zéro"

"""
Les boucles
"""

#structure iterative for avec un objet iterable.
for element in [0, 1, 2, 3, 4]:
    print(element)

#structure iterative for avec une sequence
for val in range(1,6):
    print(val)

#structure iterative while
iteration = 0
while iteration < 5:
    print("Loop:", iteration)
    iteration += 1

"""
Les chaines de caractères
"""

#opérations

#obtenir caractère, len
#upper, lower
#concaténation, substring

#formatted strings
#raw strings
#multiline
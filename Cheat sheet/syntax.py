# Types les plus utilisés en Python
var_int = 1             #type int
var_float = 3.14        #type float
var_string = "Bonjour"  #type str
var_bool = True         #type bool
var_none = None         #type NoneType

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

#opérations de casts
nombre_entier = int("45")
nombre_decimal = float("2.718")
boolean = bool(True)

#fonction qui ne fait rien
def do_nothing():
    pass

#fonction avec plusieurs paramètres
def imprimer_somme(op1: float, op2: float) -> None:
    print(op1 + op2)

#fonction avec plusieurs paramètres et une valeur de retour
def somme(op1: float, op2: float) -> float:
    return op1 + op2

#la structure conditionnelle if
def exemple_if(nombre: int) -> str:
    if nombre == 0:
        return "zéro"
    elif nombre == 1:
        return "un"
    else:
        return "autre"

#la structure conditionnelle match
def exemple_match(nombre: int):
    match nombre:
        case 0:
            return "zéro"
        case 1:
            return "un"
        case _:
            return "autre"

#expression ternaire
def exemple_expression_ternaire(nombre: int):
    "Zéro" if nombre == 0 else "Différent de zéro"

"""
Les listes
"""
liste_vide = []  #list()
ma_liste = [1,2,3]
ma_liste.append(4)      #[1, 2, 3, 4]
ma_liste.extend([5,6])  #[1, 2, 3, 4, 5, 6]
ma_liste.remove(4)      #[1, 2, 3, 5, 6]
ma_liste.pop()          #[1, 2, 3, 5]

#iteration
for element in ma_liste:
    print(element)

"""
Les tuples
"""
tuple_vide = ()  #tuple()
mon_tuple = (1,2,3)
Mon_tuple2 = 1,2,3

#unpacking
var1, var2 = (1, 2)     #var1 = 1, var2 = 2

"""
Les sets
"""
set_vide = set()
mon_set = {1, 2, 3, 3, 5}   #{1, 2, 3, 5}
mon_set.add(4)              #{1, 2, 3, 4, 5}
mon_set.pop()               #{2, 3, 4, 5}

"""
Les dictionnaires
"""
mon_dico = {1:'Un', 2:'Deux', 3:'Trois', 4:'Quatre'}
print(7 in mon_dico)    #False
print(2 in mon_dico)    #True
print(mon_dico[2])      #Deux
print(mon_dico.values())    #dict_values(['Un', 'Deux', 'Trois', 'Quatre'])
print(mon_dico.keys())      #dict_keys([1, 2, 3, 4])
print(mon_dico.items())     #dict_items([(1, 'Un'), (2, 'Deux'), (3, 'Trois'), (4, 'Quatre')])

#iteration
for cle, valeur in mon_dico.items():
    print(f"{cle} -> {valeur}")

"""
Les tableaux
"""

#importation de la librairie numpy
import numpy as np

# Création d'un tableau à partir d'une liste
array_from_list: np.ndarray[int] = np.array([1, 2, 3, 4, 5], dtype = int)
print(array_from_list)  #[1 2 3 4 5]

# Création d'un tableau multi-dimensionnel
array_2d = np.array([[1, 2, 3], [4, 5, 6]], dtype = int)

# Création d'un tableau multi-dimensionnel contenant des zéros
zeros_array = np.zeros((3, 3))

# Création d'un tableau avec une plage de valeurs
range_array = np.arange(0, 10, 2)   #[0 2 4 6 8]

# Création d'un tableau avec des valeurs aléatoires
random_array = np.random.rand(3, 3)

# Récupération d'un valeur
mon_tableau = np.array([10, 20, 30, 40, 50], dtype = int)
print(mon_tableau[2])   #30

mon_tableau_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(mon_tableau_2d[1, 2])  #6

sous_tableau = mon_tableau[1:4]     #[20 30 40]

#opérations arithmétiques
tableau1 = np.array([1, 2, 3])
tableau2 = np.array([4, 5, 6])

print(tableau1 + tableau2)  # [5 7 9]
print(tableau1 * 2)  #[2 4 6]
print(tableau1 * tableau2)  # [4 10 18]

#concaténation
print(np.concatenate((tableau1, tableau2)))     # [1 2 3 4 5 6]

#fonctions mathématiques
mon_tableau = np.array([1, 2, 3, 4, 5])
print(np.sum(mon_tableau))  # 15
print(np.min(mon_tableau))  # 1
print(np.max(mon_tableau))  # 5
print(np.mean(mon_tableau)) # 3.0

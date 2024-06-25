"""
Les opérations
"""

chaine1 = "Bonjour"
chaine2 = "Python"

# concatenation
print(chaine1 + " " + chaine2)  #Bonjour Python

# obtenir la première lettre
print(chaine1[0])   #B

# obtenir la dernière lettre
print(chaine1[-1])  #r

# obtenir les 2 premières lettres
print(chaine1[:2])  #Bo

# obtenir les 2 dernières lettres
print(chaine1[-2:]) #ur

# obtenir toutes les lettres sauf les 2 premières et les 2 dernières
print(chaine1[2:-2])    #njo

# obtenir la longueur d'une chaine de caractères
print(len(chaine1))     #7

# transformer la chaine de caractères en majuscules
print(chaine1.upper())  #BONJOUR

# transformer la chaine de caractères en minuscules
print(chaine1.lower())  #bonjour

"""
Le formatage
"""

#chaîne de caractères avec retour à la ligne
bonjour = "Bonjour\nPython"
print(bonjour)

#autre chaine avec retour à la ligne
bonjour2 = """Bonjour
Python"""
print(bonjour2)

#raw strings
print(r"C:\node\tableau")   #C:\node\tableau

#chaînes formatées
resultat = 42
print(f"Résultat: {resultat}")  

#afficher uniquement 2 chiffres après la virgule
nombre_pi = 3.141592653589793
print("nombre PI = {0:0.2f}".format(nombre_pi)) #3.14
print(f"nombre PI = {nombre_pi:0.2f}")          #3.14

#afficher avec un padding spécifique
a = 0.1234567
b = 25
print(f"{a:7.3}")   #  0.123 (padding de 7 caractères)
print(f"{b:4}")     #  25 (padding de 4 caractères)

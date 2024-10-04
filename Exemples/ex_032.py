class Mammifere:
    nom_latin = "Mamma"
    nombre_mammifere = 0
    def __init__(self):
        Mammifere.nombre_mammifere += 1

class Chien(Mammifere):
    nom_latin = "Canis Lupus Familiaris"
    def __init__(self, nom, age, race):
        super().__init__()
        self.nom = nom
        self.age = age
        self.race = race

mon_chien = Chien("Rex", 4, "Berger Allemand")
print(Mammifere.nombre_mammifere) # 1

class Chien:
    instances_chien = 0
    nom_latin = "Canis lupus familiaris"
    def __init__(self, age, nom, race):
        Chien.instances_chien += 1
        self.age = age
        self.nom = nom
        self.race = race

rex = Chien(7, "Rex", "Berger Allemand")
print(Chien.instances_chien) # 1
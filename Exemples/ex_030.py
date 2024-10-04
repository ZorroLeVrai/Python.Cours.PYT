class Chien:
    instances_chien = 0
    nom_latin = "Canis lupus familiaris"

    def __init__(self, age, nom, race):
        Chien.instances_chien += 1
        self.age = age
        self.nom = nom
        self.race = race

    @classmethod
    def afficher_nombre_chiens(cls):
        print(f"Il y a {cls.instances_chien} chien instancié(s)")

rex = Chien(7, "Rex", "Berger Allemand")
print(Chien.instances_chien)            # 1
print(Chien.afficher_nombre_chiens())   # 1

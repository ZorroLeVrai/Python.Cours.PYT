from datetime import date

class Mammifere:
    nom_latin = "Mamma"
    nombre_mammifere = 0

    def __init__(self):
        Mammifere.nombre_mammifere += 1

    def calculer_age(self, annee) -> int:
        return date.today().year - annee


class Chien(Mammifere):
    nom_latin = "Canis Lupus Familiaris"

    def __init__(self, nom, annee, race):
        super().__init__()
        self.nom = nom
        self.annee = annee
        self.race = race

    def age_chien(self) -> int:
        return super().calculer_age(self.annee)


rex = Chien("Rex", 2020, "Berger Allemand")
age_chien = rex.age_chien()
print("Age du chien:", age_chien)  # Age du chien: 4

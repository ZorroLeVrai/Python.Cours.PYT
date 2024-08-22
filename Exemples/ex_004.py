class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

class Enfant(Personne):
    def __init__(self, nom, prenom, age, jouet):
        super().__init__(nom, prenom, age)
        self.jouet = jouet

Enfant("Doe", "John", 8, "Camion")
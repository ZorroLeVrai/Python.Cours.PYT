class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

class Enfant(Personne):
    def __init__(self, nom, prenom, age, jouet):
        super().__init__(nom, prenom, age)
        self.jouet = jouet

nicolas = Enfant("Doe", "John", 8, "Camion")
# Nom: John Doe; Age: 8; Jouet: Camion
print(f"Nom: {nicolas.prenom} {nicolas.nom}; Age: {nicolas.age}; Jouet: {nicolas.jouet}")
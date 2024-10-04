class Compte:
    def __init__(self, identifiant, montant = 0):
        self.identifiant = identifiant
        self.montant = montant

    def versement(self, somme):
        self.montant += somme  # self.montant = self.montant + somme
    
    def retrait(self, somme):
        self.montant -= somme  # self.montant = self.montant - somme

    def afficher_solde(self):
        print(f"Le compte {self.identifiant} contient {self.montant} Euros")

# Utilisation de la classe Compte
compte_john = Compte("John", 200)
compte_jane = Compte("Jane", 300)
compte_john.retrait(100)
compte_jane.versement(50)
compte_john.afficher_solde()  #Le compte John contient 100 Euros
compte_jane.afficher_solde()  #Le compte Jane contient 350 Euros

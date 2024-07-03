taux_agios = 0.05

class CompteBancaire:
    """Cette classe permet de gérer un compte bancaire"""

    def __init__(self, numero_compte: str, nom: str, solde: float):
        self.numero_compte = numero_compte
        self.nom = nom
        self.solde = solde

    def versement(self, montant: float) -> None:
        self.solde += montant

    def retrait(self, montant: float) -> None:
        self.solde -= montant

    def agios(self) -> None:
        """Permet d'appliquer des agios si le solde est négatif"""
        if self.solde < 0:
            self.solde *= (1 + taux_agios)

    def afficher(self) -> None:
        """Afficher le détail du compte"""
        print("Afficher le détail du compte:")
        print(f"Numéro de compte: {self.numero_compte}")
        print(f"Nom: {self.nom}")
        print(f"Solde: {self.solde}")
        print()


if __name__ == "__main__":
    compte = CompteBancaire(123, "John", 100)
    compte.versement(50)
    compte.afficher()
    compte.retrait(200)
    compte.agios()
    compte.afficher()

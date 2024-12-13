"""
Exercice 35: Créer une classe Personne avec les attributs suivants:
- nom
- prénom
- numéro de téléphone
- email
"""

class Personne:
    """
    Classe Personne
    Contient les informations d'une personne
    """
    def __init__(self, nom: str, prenom: str, numero_tel: str, email: str):
        """
        Constructeur de la classe Personne
        """
        self.nom = nom
        self.prenom = prenom
        self.numero_tel = numero_tel
        self.email = email

    def __str__(self):
        return f"""
Nom: {self.nom}
Prénom: {self.prenom}
Numéro de Téléphone: {self.numero_tel}
Email: {self.email}"""


class Travailleur(Personne):
    """
    Classe Travailleur
    Contient les informations d'un travailleur
    """
    def __init__(self,
                 nom: str,
                 prenom: str,
                 numero_tel: str,
                 email: str,
                 nom_entreprise: str,
                 adresse_entreprise: str,
                 telephone_pro: str):
        super().__init__(nom, prenom, numero_tel, email)
        self.nom_entreprise = nom_entreprise
        self.adresse_entreprise = adresse_entreprise
        self.telephone_pro = telephone_pro

    def __str__(self):
        return f"""
{super().__str__()}
Nom entreprise: {self.nom_entreprise}
Adresse entreprise: {self.adresse_entreprise}
Téléphone pro: {self.telephone_pro}"""


class Scientifique(Travailleur):
    def __init__(self,
                 nom: str,
                 prenom: str,
                 numero_tel: str,
                 email: str,
                 nom_entreprise: str,
                 adresse_entreprise: str,
                 telephone_pro: str,
                 disciplines: list[str],
                 type_scientifique: str):
        super().__init__(nom, prenom, numero_tel, email, nom_entreprise, adresse_entreprise, telephone_pro)
        self.disciplines = disciplines
        self.type_scientifique = type_scientifique

    def __str__(self):
        return f"""
{super().__str__()}
Disciplines: {self.disciplines}
Type du scientifique: {self.type_scientifique}"""


if __name__ == "__main__":
    personne = Personne("Doe", "John", "1234", "john.doe@gmail.com")
    print(personne)

    travailleur = Travailleur("Doe", "Jane", "8888", "jane.doe@gmail.com", "Google", "Paris", "123456")
    print(travailleur)

    scientifique = Scientifique("Doe", "Jane", "8888", "jane.doe@gmail.com", "Google", "Paris", "123456", ["Physique", "Chimie"], "Théorique")
    print(scientifique)

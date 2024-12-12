class WaterTank:
    """Classe qui permet la gestion d'une citerne"""

    def __init__(self, poids_vide: float, capacite_max: float, niveau_remplissage: float):
        # Poids à vide en Kg
        self.poids_vide = poids_vide
        # Capacité max de la citerne en litres
        self.capacite_max = capacite_max
        # Niveau de remplissage de la citerne en litres
        self.niveau_remplissage = niveau_remplissage

    def get_poids_total(self) -> float:
        return self.poids_vide + self.niveau_remplissage

    def remplir_citerne(self, nb_litres: float) -> float:
        """
        Remplir la citerne

        nb_litres: Nombre de litres à ajouter
        returns: Nombre de litres réellement ajoutés
        """
        nb_litres_ajoutes = nb_litres if self.niveau_remplissage + nb_litres <= self.capacite_max \
            else self.capacite_max - self.niveau_remplissage

        self.niveau_remplissage += nb_litres_ajoutes
        return nb_litres_ajoutes

    def vider_citerne(self, nb_litres: float) -> float:
        """
        Vider la citerne

        nb_litres: Nombre de litres à enlever
        returns: Nombre de litres réellement enlevés
        """
        nb_litres_retires = nb_litres if self.niveau_remplissage - nb_litres >= 0 \
            else self.niveau_remplissage

        self.niveau_remplissage -= nb_litres_retires
        return nb_litres_retires


if __name__ == "__main__":
    citerne1 = WaterTank(100, 1000, 0)
    citerne2 = WaterTank(100, 1000, 0)
    print("Citerne 1 poids:", citerne1.get_poids_total())
    print("Citerne 2 poids:", citerne2.get_poids_total())

    citerne1.remplir_citerne(250)
    citerne2.remplir_citerne(500)
    print("Citerne 1 poids:", citerne1.get_poids_total())
    print("Citerne 2 poids:", citerne2.get_poids_total())


class VolDirect:
    def __init__(self, dep: str, arr: str, jour: str, heure: int) -> None:
        self.dep = dep
        self.arr = arr
        self.jour = jour
        self.heure = heure

    def afficher(self):
        print(f"Ce vol part de {self.dep} vers {self.arr} le {self.jour} à {self.heure} heure")


class Vols:
    def __init__(self, liste_vol: list[VolDirect]) -> None:
        self.liste_vol = liste_vol

    def afficher_successeurs(self, ville_depart: str):
        vols_concernes = filter(lambda vd: vd.dep == ville_depart, self.liste_vol)
        successeurs =  list(map(lambda vd: vd.arr, vols_concernes))
        print(f"La liste des destinations à partir de {ville_depart} est: {successeurs}")
    
    def afficher_appartenance(self, ville: str):
        appartient = any(map(lambda vd: vd.dep == ville or vd.arr == ville, self.liste_vol))
        if appartient:
            print(f"La ville {ville} fait partie du plan de vol!")
        else:
            print(f"La ville {ville} ne fait pas partie du plan de vol!")

    
    def afficher(self):
        print("=== Liste des vols ===")
        for vol_direct in self.liste_vol:
            vol_direct.afficher()


if __name__ == "__main__":
    lv: list[VolDirect] = []
    lv.append(VolDirect("Paris", "Marseille", "17/9", 4))
    lv.append(VolDirect("Paris", "Lyon", "21/9", 8))
    lv.append(VolDirect("Marseille", "Lyon", "11/9", 17))
    lv.append(VolDirect("Paris", "Bruxelles", "4/9", 20))

    v = Vols(lv)
    v.afficher()
    print()
    v.afficher_appartenance("Paris")
    v.afficher_appartenance("Bruxelles")
    v.afficher_appartenance("Bordeaux")
    print()
    v.afficher_successeurs("Paris")

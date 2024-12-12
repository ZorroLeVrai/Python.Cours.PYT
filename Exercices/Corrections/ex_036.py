from itertools import combinations

class Element:
    def __init__(self, valeur: int, postfixe: str, infixe: str):
        self.valeur = valeur
        self.postfixe = postfixe
        self.infixe = infixe

    def __str__(self):
        return f"[{self.postfixe}:{self.valeur}]"
    
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, other):
        return Element(self.valeur + other.valeur, f"{self.postfixe} {other.postfixe} +", f"({self.infixe}+{other.infixe})")

    def __sub__(self, other):
        return Element(self.valeur - other.valeur, f"{self.postfixe} {other.postfixe} -", f"({self.infixe}-{other.infixe})")

    def __mul__(self, other):
        return Element(self.valeur * other.valeur, f"{self.postfixe} {other.postfixe} *", f"({self.infixe}*{other.infixe})")

    def __truediv__(self, other):
        return Element(self.valeur // other.valeur, f"{self.postfixe} {other.postfixe} /", f"({self.infixe}/{other.infixe})")
    
    def __ge__(self, other):
        return self.valeur >= other.valeur
    
    def calculer_distance(self, cible: int):
        return abs(self.valeur - cible)


class MeilleurSolution:
    def __init__(self, element: Element, distance: int):
        self.solution = element
        self.distance = distance

    def __str__(self):
        return f"{self.solution} - Distance: {self.distance}"
    
    def __repr__(self):
        return self.__str__()
    
    def retourner_meilleur(self, element: Element, cible: int):
        distance = element.calculer_distance(cible)
        if distance < self.distance:
            return MeilleurSolution(element, distance)
        else:
            return self


def creer_element(valeur: int):
    return Element(valeur, str(valeur), str(valeur))

def calculer(element_gauche: Element, element_droite: Element, operateur: str):
    match operateur:
        case "+":
            return element_gauche + element_droite
        case "-":
            return element_gauche - element_droite
        case "*":
            return element_gauche * element_droite
        case "/":
            return element_gauche / element_droite
        case _:
            raise ValueError("Opérateur non supporté")

def simuler_operation(elements: list[Element], position_gauche: int, position_droite: int, operateur: str, cible: int, meilleur_solution: MeilleurSolution) -> tuple[list[Element], MeilleurSolution]:
    nouvel_element = calculer(elements[position_gauche], elements[position_droite], operateur)
    meilleur_solution = meilleur_solution.retourner_meilleur(nouvel_element, cible)
    elements_copie = elements.copy()
    del elements_copie[position_gauche, position_droite]
    elements_copie.append(nouvel_element)
    return elements_copie, meilleur_solution
    

def resoudre(elements: list[Element], cible: int) -> MeilleurSolution:
    def resoudre_loc(elements: list[Element], meilleur_solution: MeilleurSolution) -> MeilleurSolution:
        nb_elements = len(elements)
        if nb_elements == 1:
            return meilleur_solution.retourner_meilleur(elements[0], cible)

        solutions = []

        # On commence par générer toutes les combinaisons possibles
        for op_gauche, op_droite in combinations(range(nb_elements), 2):
            # Plus
            _elements, _meilleur_solution = simuler_operation(elements, op_gauche, op_droite, "+", cible, meilleur_solution)
            solutions.append(resoudre_loc(_elements, _meilleur_solution))
            # Moins gauche, droite
            _elements, _meilleur_solution = simuler_operation(elements, op_gauche, op_droite, "-", cible, meilleur_solution)
            solutions.append(resoudre_loc(_elements, _meilleur_solution))
            # Moins droite, gauche
            _elements, _meilleur_solution = simuler_operation(elements, op_droite, op_gauche, "-", cible, meilleur_solution)
            solutions.append(resoudre_loc(_elements, _meilleur_solution))
            # Multiplier
            _elements, _meilleur_solution = simuler_operation(elements, op_gauche, op_droite, "*", cible, meilleur_solution)
            solutions.append(resoudre_loc(_elements, _meilleur_solution))
            # Diviser
            if op_gauche >= op_droite:
                _elements, _meilleur_solution = simuler_operation(elements, op_gauche, op_droite, "/", cible, meilleur_solution)
            else:
                _elements, _meilleur_solution = simuler_operation(elements, op_droite, op_gauche, "/", cible, meilleur_solution, meilleur_distance)
            solutions.append(resoudre_loc(_elements, _meilleur_solution))

        return min(solutions, key=lambda x: x.distance)

    if elements:
        element_solutions: list[MeilleurSolution] = map(lambda x: MeilleurSolution(x, x.calculer_distance(cible)), elements)
        meilleur_solution = min(element_solutions, key=lambda x: x.distance)
        return resoudre_loc(elements, meilleur_solution)
    else:
        print("Pas de solution")
        return None


meilleur_solution = resoudre([creer_element(10), creer_element(5)], 5)
print(meilleur_solution.solution)
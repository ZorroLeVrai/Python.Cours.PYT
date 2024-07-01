from functools import reduce

nom_fichier = "texte.txt"

def lire_fichier(nom_fichier: str) -> str:
    with open(nom_fichier, "r") as fichier:
        return fichier.read()


def get_nb_occurence_dict(text: str) -> dict[str, int]:
    def add_word(accumulator: dict[str, int], current: str) -> dict[str, int]:
        nb_occurence = accumulator.get(current)
        if nb_occurence:
            accumulator[current] = nb_occurence + 1
        else:
            accumulator[current] = 1
        
        return accumulator


    words = text.split()
    return reduce(add_word, words, dict())


texte = lire_fichier(nom_fichier)
occurence_dico = get_nb_occurence_dict(texte)
occurence_dico = dict(sorted(occurence_dico.items(), key=lambda item: item[1], reverse=True))
print(occurence_dico)

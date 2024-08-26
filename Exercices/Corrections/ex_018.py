import re
from functools import reduce

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


    words: list[str] = re.split("[ ,;.\n]", text)
    empty_words_filtered = filter(lambda w: w, words)
    small_letters_words = map(lambda w: w.lower(), empty_words_filtered)
    return reduce(add_word, small_letters_words, dict())


if __name__ == "__main__":
    nom_fichier = "texte.txt"
    texte = lire_fichier(nom_fichier)
    occurence_dico = get_nb_occurence_dict(texte)
    occurence_dico = dict(sorted(occurence_dico.items(), key=lambda item: item[1], reverse=True))
    print(occurence_dico)

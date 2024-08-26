import sys

def generateur_alphabet(est_majuscule: bool) -> str:
    resultat = ""
    ascii_char_debut = ord('A') if est_majuscule else ord('a')
    for ascii_char in range(ascii_char_debut, ascii_char_debut+26):
        resultat += chr(ascii_char)
    return resultat


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise RuntimeError("Vous devez spécifier un argument à ce programme")

    match sys.argv[1]:
        case "minuscule":
            print(generateur_alphabet(False))
        case "majuscule":
            print(generateur_alphabet(True))
        case _:
            raise RuntimeError("Argument inconnu")

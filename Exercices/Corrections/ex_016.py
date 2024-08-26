message_saisie = "Veuillez entrer une note entre 0 et 20 compris (une note négative stoppera la saisie): "

def saisir_une_note() -> float:
    while True:
        note_str = input(message_saisie)
        try:
            note = float(note_str)
            if note > 20:
                print("Veuillez saisir un nombre inférieur ou égal à 20")
            else:
                return note
        except ValueError:
            print("Veuillez saisir un nombre entier ou un nombre décimal")


def saisir_notes() -> tuple[float, float, float]:
    note_minimale: float = 20
    note_maximale: float = 0
    somme_notes: float = 0
    nb_notes: int = 0

    while True:
        note = saisir_une_note()
        if note < 0:
            break

        if note < note_minimale:
            note_minimale = note

        if note > note_maximale:
            note_maximale = note
        
        somme_notes += note
        nb_notes += 1

    moyenne = somme_notes / nb_notes if nb_notes > 0 else 0
    return (note_minimale, note_maximale, moyenne)


if __name__ == "__main__":
    (note_min, note_max, moyenne) = saisir_notes()
    print(f"La note minimale est de {note_min} / 20")
    print(f"La note maximale est de {note_max} / 20")
    print(f"La moyenne est de {moyenne} / 20")

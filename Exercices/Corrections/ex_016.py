message_saisie = "Veuillez entrer une note entre 0 et 20 compris (une note négative stoppera la saisie): "

def saisir_une_note() -> float:
    while True:
        note = float(input(message_saisie))
        if note > 20:
            print("Veuillez saisir un nombre inférieur ou égal à 20")
        else:
            return note
        
def saisir_notes() -> list[float]:
    notes = []
    while True:
        note = saisir_une_note()
        if note < 0:
            break
        notes.append(note)
    return notes


notes = saisir_notes()
print(f"La note minimale est de {min(notes)} / 20")
print(f"La note maximale est de {max(notes)} / 20")
print(f"La moyenne est de {sum(notes) / len(notes)} / 20")
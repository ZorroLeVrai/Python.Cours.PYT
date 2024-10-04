class Eleve:
    def __init__(self, nom):
        self.nom = nom
        self.notes = dict()

    def ajouter_note(self, matiere, note):
        self.notes[matiere] = note

    def supprimer_note(self, matiere):
        del self.notes[matiere]

    def voir_notes(self):
        print(self.notes)

john = Eleve("John")

john.ajouter_note("Math", 12)
john.ajouter_note("Français", 14)
john.voir_notes()  # {'Math': 12, 'Français': 14}
john.supprimer_note("Français")
john.voir_notes()  # {'Math': 12}

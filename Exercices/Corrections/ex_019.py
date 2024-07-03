from collections.abc import Iterator

def generateur_alphabet(est_majuscule: bool) -> Iterator[str]:
    ascii_char_debut = ord('A') if est_majuscule else ord('a')
    for ascii_char in range(ascii_char_debut, ascii_char_debut+26):
        yield chr(ascii_char)

gen_alphabet = generateur_alphabet(False)
print(list(gen_alphabet))

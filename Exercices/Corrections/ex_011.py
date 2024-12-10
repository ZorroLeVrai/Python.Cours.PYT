def inverser_chaine(text: str) -> str:
    chaine_inversee = ""
    longeur_chaine = len(text)
    for index in range(longeur_chaine-1, -1, -1):
        chaine_inversee += text[index]

    return chaine_inversee

def inverser_chaine_v2(text: str) -> str:
    chaine_inversee = ""
    longeur_chaine = len(text)
    for index in range(-1, -1*longeur_chaine-1, -1):
        chaine_inversee += text[index]

    return chaine_inversee

def inverser_chaine_v3(text: str) -> str:
    chars = list(text)
    chars.reverse()
    return "".join(chars)

def inverser_chaine_v4(text: str) -> str:
    return text[::-1]


texte = "Bonjour"
print(inverser_chaine(texte))
print(inverser_chaine_v2(texte))
print(inverser_chaine_v3(texte))
print(inverser_chaine_v4(texte))

#Rechercher des numéro de téléphone au format "XXX-XXX-XXXX"
import re

# Définir une chaîne de caractères
text = "Mon numéro de téléphone est 123-456-7890."

# Rechercher tous les numéro de téléphone
numero_tel = re.findall(r"\d{3}-\d{3}-\d{4}", text)

if numero_tel:
    print(f"Numéro(s) de téléphone trouvé(s): {numero_tel}")
else:
    print("Aucun numéro de téléphone trouvé")

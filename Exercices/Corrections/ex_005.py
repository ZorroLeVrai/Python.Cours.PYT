age = int(input("Saisir age: "))
salaire_euros = float(input("Saisir le salaire souhaité (En Euros): "))
annees_experience = int(input("Saisir le nombre d'années d'expérience: "))

conditions_poste = True
if age < 30:
    print("L'âge minimum pour le poste est 30 ans.")
    conditions_poste = False

if salaire_euros > 40_000:
    print("Le salaire maximum possible est 40 000 euros.")
    conditions_poste = False

if annees_experience < 5:
    print("Le nombre d'années d'expérience minimum est de 5 ans.")
    conditions_poste = False

if conditions_poste:
    print("Toutes les conditions sont respectées pour le poste")

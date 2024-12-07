temperature = float(input("Entrez la température de l'eau: "))
etat = "solide" if temperature < 0 else ("liquide" if temperature <= 100 else "gazeux")
print(etat)
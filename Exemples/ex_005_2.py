# Vérifiez si l'eau est à l'état liquide
temperature_eau = float(input("Entrez la température de l'eau: "))
eau_liquide = (temperature_eau >= 0) and (temperature_eau < 100)
print("L'eau est t-elle à l'état liquide:", eau_liquide)

temp_celsius = float(input("Entrez la température de l'eau en °C: "))

if temp_celsius < 0:
    etat_eau = "SOLIDE"
elif temp_celsius <= 100:
    etat_eau = "LIQUIDE"
else:
    etat_eau = "GAZEUX"

print(etat_eau)

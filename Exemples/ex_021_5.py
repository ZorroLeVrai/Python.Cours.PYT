salaires = [1200, 2500, 1950, 850, 2000, 1700]
# A l'aide de la fonction map, appliquez une augmentation de 5%
nouveau_salaires = map(lambda x: x*1.05, salaires)
# A l'aide de la fonction filtrer, filtrez uniquement les nouveaux salaires de plus de 2000 Euros
salaires_filtres = filter(lambda x: x > 2000, nouveau_salaires)
# Affichage uniquement des nouveaux salaires supérieurs à 2000 Euros
print(list(salaires_filtres))   #[2625.0, 2047.5, 2100.0]

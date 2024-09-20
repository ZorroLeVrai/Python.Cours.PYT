import pandas as pd

# Lire les fichiers CSV
df1 = pd.read_csv('fichier1.csv')
df2 = pd.read_csv('fichier2.csv')

# Fusionner les deux DataFrames (par défaut, axis=0 pour concaténer verticalement)
df_fusionne = pd.concat([df1, df2], ignore_index=True)

# Sauvegarder le DataFrame fusionné dans un fichier CSV
df_fusionne.to_csv('fichier_fusionne.csv', index=False)

print("Les DataFrames ont été fusionnés et sauvegardés avec succès.")

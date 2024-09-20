import pandas as pd
import os
import glob

# Spécifiez le répertoire où chercher les fichiers
repertoire_source = r".\Data"
# Spécifiez le format des fichiers à inclure
format_fichiers_source = "villes_*.csv"
# Spécifier l'emplacement du fichier cible
fichier_cible = r".\Output\villes.csv"

# Utiliser glob pour trouver tous les fichiers correspondant au modèle "villes_*.csv"
fichiers_csv = glob.glob(os.path.join(repertoire_source, format_fichiers_source))

# Transformation de la liste de noms de fichier en liste de DataFrame
df_liste = [pd.read_csv(fichier) for fichier in fichiers_csv]
#df_liste = list(map(lambda fichier:pd.read_csv(fichier), fichiers_csv))

#fusionner la liste des dataframes
df_fusionne = pd.concat(df_liste, ignore_index=True)

# Sauvegarder le DataFrame fusionné dans un fichier CSV
df_fusionne.to_csv(fichier_cible, index=False)

print("Les DataFrames ont été fusionnés et sauvegardés avec succès.")

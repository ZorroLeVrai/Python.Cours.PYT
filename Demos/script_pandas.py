import pandas as pd

repertoire = r"D:\Users\amine\Documents\GitHub\Python.Bureautique\Notebooks\Exercices\Data\Reseaux"
fichier_utilisateurs = repertoire + "\\utilisateurs.csv"
fichier_temps_passe = repertoire + "\\reseaux_sociaux.csv"

df_utilisateurs = pd.read_csv(fichier_utilisateurs, encoding="latin-1")
df_donnees = pd.read_csv(fichier_temps_passe, encoding="latin-1")

df_utilisateurs.rename(columns={'id': 'id_utilisateur'}, inplace=True)
df_donnees.rename(columns={'id': 'id_data'}, inplace=True)

df_merge = df_utilisateurs.merge(df_donnees, on="adresse IP", how="left")

df_merge.to_csv("output.csv")

print("Fichier créé")

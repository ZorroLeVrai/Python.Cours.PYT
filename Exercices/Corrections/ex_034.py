"""
Déplacer les fichiers de test dans un répertoire spécifique
"""
import os
import glob


# Spécifiez le répertoire où chercher les fichiers
REPERTOIRE_SOURCE = r"D:\Users\amine\Documents\GitHub\Python.Cours.PYT\Exercices\Repertoire"
# Spécifiez le format des fichiers à inclure
FORMAT_FICHIERS_SOURCE = "test_*.py"
REPERTOIRE_CIBLE = "tests"


def deplacer_fichier_dans_tests(file_paths: list[str], target_dir: str) -> None:
    """Déplacer les fichiers spécifiés dans le répertoire cible"""
    for file_path in file_paths:
        # Récupérer le nom du répertoire et le nom du fichier
        dir_path, file_name = os.path.split(file_path)

        # Ajouter le répertoire cible au nom du répertoire courant
        tests_dir = os.path.join(dir_path, target_dir)

        # Créer le répertoir cible si celui-ci n'existe pas
        if not os.path.exists(tests_dir):
            os.makedirs(tests_dir)

        # Le chemin cible à utiliser pour déplacer le fichier
        dest_path = os.path.join(tests_dir, file_name)

        # Déplacement du fichier
        os.rename(file_path, dest_path)
        print(f"Déplacement du fichier {file_name} vers {tests_dir}")


# Utiliser glob pour trouver tous les fichiers correspondant au modèle "villes_*.csv"
# fichier_a_deplace = glob.glob("..\Repertoire\test_*.py")
format_fichier_a_deplacer = os.path.join(REPERTOIRE_SOURCE, FORMAT_FICHIERS_SOURCE)
fichiers_a_deplacer = glob.glob(format_fichier_a_deplacer)

deplacer_fichier_dans_tests(fichiers_a_deplacer, REPERTOIRE_CIBLE)

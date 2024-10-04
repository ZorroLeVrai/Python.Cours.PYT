import os
import glob

# Spécifiez le répertoire où chercher les fichiers
repertoire_source = r"..\Repertoire"
# Spécifiez le format des fichiers à inclure
format_fichiers_source = "test_*.py"
repertoire_cible = "tests"


def deplacer_fichier_dans_tests(file_paths, target_dir):
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
        print(f"Déplacement de {file_name} vers {tests_dir}")


# Utiliser glob pour trouver tous les fichiers correspondant au modèle "villes_*.csv"
fichiers_a_deplacer = glob.glob(os.path.join(repertoire_source, format_fichiers_source))

deplacer_fichier_dans_tests(fichiers_a_deplacer)

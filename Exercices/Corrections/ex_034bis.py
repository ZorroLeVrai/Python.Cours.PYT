import os

# Chemin du répertoire source
source_dir = 'Repertoire'

# Créer le répertoire 'tests' s'il n'existe pas
tests_dir = os.path.join(source_dir, 'tests')
if not os.path.exists(tests_dir):
    os.makedirs(tests_dir)

# Parcourir les fichiers du répertoire source
for file_name in os.listdir(source_dir):
    # Vérifier si le fichier commence par 'test_' et se termine par '.py'
    if file_name.startswith('test_') and file_name.endswith('.py'):
        # Construire le chemin complet source et destination
        source_path = os.path.join(source_dir, file_name)
        destination_path = os.path.join(tests_dir, file_name)
        
        # Déplacer le fichier
        os.rename(source_path, destination_path)
        print(f"Fichier déplacé: {file_name}")

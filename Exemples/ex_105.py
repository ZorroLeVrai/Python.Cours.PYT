import os
import shutil as su

def obtenir_repertoire_courant():
    """Retourne le répertoire courant"""
    return os.getcwd()

def changer_repertoire_courant(chemin):
    """Modifie le répertoire courant"""
    os.chdir(chemin)

def lister_fichiers_repertoires(chemin):
    """Liste les fichiers et les répertoires"""
    return os.listdir(chemin)

def creer_repertoire(nom_repertoire):
    """Crée un répertoire"""
    os.mkdir(nom_repertoire)

def supprimer_fichier(chemin_fichier):
    """Supprime un fichier"""
    os.remove(chemin_fichier)

def supprimer_repertoire_vide(chemin_repertoire):
    """Supprime un répertoire vide"""
    os.rmdir(chemin_repertoire)

def supprimer_repertoire_et_contenu(chemin_repertoire):
    """Supprime un répertoire et son contenu"""
    if os.path.exists(chemin_repertoire):
        su.rmtree(chemin_repertoire)
        print(f"Le répertoire '{chemin_repertoire}' et son contenu ont été supprimés.")
    else:
        print(f"Le répertoire '{chemin_repertoire}' n'existe pas.")

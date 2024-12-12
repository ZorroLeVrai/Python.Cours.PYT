import sys

if len(sys.argv) < 4:
    print("Vous devez spéficier 3 paramètres")
    print("Usage: python concat.py fichier1 fichier2 fichier3")
    exit(1)

fichier1 = sys.argv[1]
fichier2 = sys.argv[2]
output = sys.argv[3]

with open(fichier1, 'r') as f1, open(fichier2, 'r') as f2, open(output, 'w') as out:
    contenu_fichier1 = f1.read()
    contenu_fichier2 = f2.read()
    
    out.write(contenu_fichier1)
    out.write("\n")
    out.write(contenu_fichier2)
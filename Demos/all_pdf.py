import sys
import os

if len(sys.argv) < 2:
    raise TypeError("Vous devez spéficier le répertoire")

directory = "D:\\temp"
directory = sys.argv[1]

# List to store PDF file names
pdf_files = []

# Iterate over files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        pdf_files.append(filename)

# Print the list of PDF files
print("Fichiers PDF dans le répertoire:")
for pdf_file in pdf_files:
    print(pdf_file)

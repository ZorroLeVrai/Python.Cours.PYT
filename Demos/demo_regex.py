import re

# Chaine de caractères à modifier
text = "The rain in Spain stays mainly in the plain."

# Pattern à remplacer
pattern = r"ain"

# Pattern de remplacement
replacement = "XYZ"

# Remplacement du pattern
new_text = re.sub(pattern, replacement, text)

print(new_text)

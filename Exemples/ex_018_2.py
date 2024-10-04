# Unifiez 2 listes d'invités
# Définir les deux listes d'invités (les listes d'invités sont définies en tant que set)
set_A = {"Alice", "Bob", "Charlie", "David", "Emma"}
set_B = {"Bob", "David", "Fiona", "George", "Alice"}

# Unifier les deux sets en utilisant l'opération d'union
set_unifie = set_A.union(set_B)

# Afficher la liste des invités
print("Invités uniques :", set_unifie)

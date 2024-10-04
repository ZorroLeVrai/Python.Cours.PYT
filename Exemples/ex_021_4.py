lst = [1, 2, 3, 4, 5, 6]
#utilisation de map pour modifier chaque élément de la liste
squares = map(lambda x: x*x, lst)
print(list(squares))    #[1, 4, 9, 16, 25, 36]
#utilisation de filter pour filtrer les éléments de la liste
filtered = filter(lambda x: x % 2 == 1, lst)
print(list(filtered))   #[1, 3, 5]

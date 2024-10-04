liste_vide = []
ma_liste = [2, 1, 3]
#[2, 1, 3]
print(ma_liste)
ma_liste.sort()
#[1, 2, 3]
print(ma_liste)
ma_liste.append(4)
#[1, 2, 3, 4]
print(ma_liste)
ma_liste.extend([5,6])
#[1, 2, 3, 4, 5, 6]
print(ma_liste)
ma_liste.remove(4)
#[1, 2, 3, 5, 6]
print(ma_liste)
ma_liste.pop()
#[1, 2, 3, 5]
print(ma_liste)

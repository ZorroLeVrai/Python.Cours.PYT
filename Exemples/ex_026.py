class MaClasse:
    """une classe"""
    test = 0
    def __init__(self):
        self.test1 = 1

cl = MaClasse()
# Classe
print(MaClasse.__name__)    # MaClasse
print(MaClasse.__doc__)     # une classe
print(MaClasse.__dict__)    # {'test': 0, .....}
print(MaClasse.__bases__)   # (<class 'object'>,)
print(MaClasse.__module__)  # __main__
# Instance
print(cl.__class__)             # <class '__main__.MaClasse'>
print(cl.__class__.__name__)    # MaClasse
print(cl.__dict__)              # {'test1': 1}
print(cl.__doc__)               # une classe

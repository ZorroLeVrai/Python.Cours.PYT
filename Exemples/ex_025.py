class Chien:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

rex = Chien("Rex", 11)
print("Age du chien:", rex.age)  #Age du chien: 11
rex.age = 12
print("Age du chien:", rex.age)  #Age du chien: 12

class Person:
    def __init__(self, name, age):
        self._name = name

    # Getter pour l'attribut 'name'
    @property
    def name(self):
        return self._name

    # Setter pour l'attribut 'name'
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value


person = Person("Alice", 30)

# Utilisation du getter
print(person.name)  # Alice

# Utilisation du setter
person.name = "Bob"
print(person.name)  # Bob

# Affectation d'un nom vide (provoque une erreur)
try:
    person.name = ""
except ValueError as e:
    print(e)  # Name cannot be empty

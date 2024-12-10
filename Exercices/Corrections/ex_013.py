def transformation_fizz_buzz(nombre: int) -> str:
    resultat = ""
    if nombre % 3 == 0:
        resultat += "Fizz"
    if nombre % 5 == 0:
        resultat += "Buzz"

    # if resultat == ""
    if not resultat:
        resultat = str(nombre)

    return resultat

def fizz_buzz(nombre_max: int) -> list[str]:
    result = []
    for nombre in range(1, nombre_max+1):
        result.append(transformation_fizz_buzz(nombre))
    return result

def fizz_buzz_v2(nombre_max: int) -> list[str]:
    return list(map(transformation_fizz_buzz, range(1, nombre_max+1)))

def fizz_buzz_v3(nombre_max: int) -> list[str]:
    return [transformation_fizz_buzz(nombre) for nombre in range(1, nombre_max+1)]

print("Calcul FizzBuzz")
nb = int(input("Saisissez un nombre entre 1 et 100: "))
resultats = fizz_buzz(nb)
for resultat in resultats:
    print(resultat)

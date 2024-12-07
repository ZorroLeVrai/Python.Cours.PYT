#action: Callable[[float], None]
def calcul_puis_action(action):
    resultat = 17
    action(resultat)


calcul_puis_action(lambda result: print(f"Résultat: {result}"))

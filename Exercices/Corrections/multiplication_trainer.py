import time
import random

def ask_multiplication(x: int, y: int) -> bool:
    saisie = int(input(f"Calulez {x} x {y}: "))
    resultat = x*y
    if saisie == resultat:
        print("Bonne réponse")
        return True
    else:
        print(f"Faux! {x} x {y} = {resultat}")
        return False


def simulate_multiplication_drills(multplication_tables: list[int], nb_operations: int) -> tuple[int, float]:
    nb_good_responses = 0
    start_time = time.time()
    for index in range(nb_operations):
        if ask_multiplication(random.choice(multplication_tables), random.randint(1,10)):
            nb_good_responses += 1

    end_time = time.time()
    return (nb_good_responses, end_time - start_time)


multplication_tables = [1,2,3,4,5]
nb_operations = 10

nb_good_responses, elapsed_time = simulate_multiplication_drills(multplication_tables, nb_operations)
print(f"Nombre de bonnes réponses: {nb_good_responses} / {nb_operations}")
print(f"Temps total écoulé {round(elapsed_time, 2)}s")

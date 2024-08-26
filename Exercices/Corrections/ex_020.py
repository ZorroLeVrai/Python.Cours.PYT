from collections.abc import Callable

def decorer_fonction(func: Callable[[], None]) -> Callable[[], None]:
    def fonction_locale() -> None:
        print("Avant la décoration")
        func()
        print("Après la décoration")

    return fonction_locale

@decorer_fonction
def fonction_base_decoree() -> None:
    fonction_base()

def fonction_base() -> None:
    print("Je suis la fonction de base")

# def simuler_decorateur() -> None:
#     decorer_fonction(fonction_base)()

if __name__ == "__main__":
    fonction_base_decoree()

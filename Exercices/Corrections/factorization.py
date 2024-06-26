def divider_generator_factory():
    yield 2
    current_divider = 3
    while True:
        yield current_divider
        current_divider += 2


def factorize(number: int) -> list[int]:
    factors: list[int] = []
    divider_generator = divider_generator_factory()
    current_divider = next(divider_generator)
    while number >= current_divider * current_divider:
        if (number % current_divider == 0):
            factors.append(current_divider)
            number //= current_divider
        else:
            current_divider = next(divider_generator)
    
    factors.append(number)
    return factors


def print_factorization(factors: list[int]):
    format_element = lambda factor,nb: str(factor) if nb == 1 else f"{factor}^{nb}"

    formated_factors: list[str] = []
    previous_factor = 0
    nb_occurence = 0
    for factor in factors:
        if factor == previous_factor:
            nb_occurence += 1
        else:
            if previous_factor:
                formated_factors.append(format_element(previous_factor, nb_occurence))
            previous_factor = factor
            nb_occurence = 1
    
    formated_factors.append(format_element(previous_factor, nb_occurence))
    print(" * ".join(formated_factors))


number_to_factorize = int(input("Entrez un nombre: "))
nombre_factorise = factorize(number_to_factorize)
print_factorization(nombre_factorise)
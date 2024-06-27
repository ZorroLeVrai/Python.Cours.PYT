def fibonacci_iterative(n: int) -> int:
    if n < 2:
        return n
    previous = 0
    current = 1
    for _ in range(2, n+1):
        [current, previous] = [current + previous, current]

    return current


def fibonacci_recursive(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_tail_recursive(n: int) -> int:
    def fibonacci_local(current_term: int, current: int, previous: int) -> int:
        if current_term == n:
            return current
        return fibonacci_local(current_term+1, current+previous, current)
    
    if n < 2:
        return n
    return fibonacci_local(2, 1, 1)


if __name__ == "__main__":
    nb_terme = 11
    print(fibonacci_iterative(nb_terme))
    print(fibonacci_recursive(nb_terme))
    print(fibonacci_tail_recursive(nb_terme))

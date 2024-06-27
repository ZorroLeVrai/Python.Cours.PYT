from sympy import symbols, solve

def get_remaining_principal(mortgage: float, monthly_instalment: float, time_in_months: int, annual_rate: float) -> float:
    remaining_principal = mortgage
    for _ in range(time_in_months):        
        interest_payment = remaining_principal * annual_rate/12
        remaining_principal += interest_payment - monthly_instalment

    return remaining_principal

def monthly_instalment_scenario():
    mortgage = 200_000
    nb_months = 20*12
    rate = 0.037
    monthly_instalment = symbols("monthly_instalment")
    print("Mensualité: ", solve(get_remaining_principal(mortgage, monthly_instalment, nb_months, rate)))


def borrowing_capacity_scenario():
    max_monthly_instalment = 2000
    nb_months = 25*12
    rate = 0.04
    max_mortgage = symbols("max_mortgage")
    print("Capacité d'emprunt: ", solve(get_remaining_principal(max_mortgage, max_monthly_instalment, nb_months, rate)))


if __name__ == "__main__":
    monthly_instalment_scenario()
    borrowing_capacity_scenario()
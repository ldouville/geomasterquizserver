import random


def get_ordered_random_numbers(nb_max, forbidden_numbers, quantity=3):
    if type(forbidden_numbers) is int:
        forbidden_numbers = [forbidden_numbers]
    random_numbers = []
    while len(random_numbers)  < quantity:
        x = random.randrange(1, nb_max + 1)
        if x not in forbidden_numbers + random_numbers:
            random_numbers.append(x)
    random_numbers.sort()
    return random_numbers
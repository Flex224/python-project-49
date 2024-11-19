from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def make_game():
    number = randint(1, 100)
    question = str(number)

    if is_prime(number) is False:
        return question, 'no'
    else:
        return question, 'yes'

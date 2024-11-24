from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_expression():
    random_number1 = randint(0, 100)
    random_number2 = randint(0, 100)
    question = f"{random_number1} {random_number2}"
    correct_answer = gcd(random_number1, random_number2)
    return question, str(correct_answer)

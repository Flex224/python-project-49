from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_game():
    number = randint(1, 100)
    question = (number)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, str(correct_answer)

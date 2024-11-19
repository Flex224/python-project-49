from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def make_game():
    operator = choice(['+', '-', '*'])
    random_num1 = randint(1, 10)
    random_num2 = randint(1, 10)

    if operator == '+':
        correct_answer = random_num1 + random_num2
    elif operator == '-':
        correct_answer = random_num1 - random_num2
    elif operator == '*':
        correct_answer = random_num1 * random_num2
    question = f"{random_num1} {operator} {random_num2}"
    return question, str(correct_answer)

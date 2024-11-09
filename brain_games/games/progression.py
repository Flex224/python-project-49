from random import randint
from brain_games.cli import welcome_user


def generate_progression():
    progression = []
    first_number = randint(1, 20)
    step = randint(1, 10)
    length = randint(5, 10)
    for _ in range(length):
        progression.append(first_number)
        first_number += step
    correct_answer = progression[randint(0, len(progression) - 1)]
    hidden_index = progression.index(correct_answer)
    progression[hidden_index] = '..'
    return progression, correct_answer


def progression_game():
    name = welcome_user()
    print('What number is missing in the progression?')
    right_answers = 0
    while right_answers < 3:
        progression, correct_answer = generate_progression()
        print(f'Question: {progression}')
        user_answer = int(input('Your answer: '))

        if user_answer == correct_answer:
            print('Correct!')
            right_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}")
            right_answers = 0

        if right_answers == 3:
            print(f'Congratulations, {name}!')

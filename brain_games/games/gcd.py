import random
import math
from brain_games.cli import welcome_user


def gcd_game():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    right_answers = 0
    while right_answers < 3:
        random_number1 = random.randint(0, 100)
        random_number2 = random.randint(0, 100)
        print(f"Question: {random_number1} {random_number2}")
        user_answer = int(input('Your answer: '))
        correct_answer = math.gcd(random_number1, random_number2)
        if user_answer == (correct_answer):
            print('Correct!')
            right_answers += 1
        else:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer was {correct_answer}")
            print(f"Let's try again, {name}")
            right_answers = 0
        if right_answers == 3:
            print(f'Congratulations, {name}!')

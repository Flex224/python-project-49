import random
from brain_games.cli import welcome_user


def calc():
    name = welcome_user()
    print('What is the result of the expression?')
    right_answers = 0
    while right_answers < 3:
        operator = random.choice(['+', '-', '*'])
        random_num1 = random.randint(1, 10)
        random_num2 = random.randint(1, 10)
        task = f"{random_num1} {operator} {random_num2}"
        correct_answer = eval(task)
        user_answer = int(input(f"Question: {task}\nYour answer : "))

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

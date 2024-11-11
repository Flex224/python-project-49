from random import randint
from brain_games.cli import welcome_user


def prime_game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    right_answers = 0
    while right_answers < 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = input('Your answer: ')
        if is_prime(random_number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if user_answer == correct_answer:
            print('Correct!')
            right_answers += 1
        else:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer was {correct_answer}")
            print(f"Let's try again, {name}!")
            right_answers = 0
        if right_answers == 3:
            print(f'Congratulations, {name}!')


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

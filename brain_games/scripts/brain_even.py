import random
import prompt


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')
print('Answer "yes" if the number is even, otherwise answer "no".')


def even_game(name):
    right_answers = 0
    while right_answers < 3:
        random_number = random.randint(0, 100)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        if user_answer == answer:
            print('Correct!')
            right_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            right_answers = 0
        if right_answers == 3:
            print(f'Congratulations, {name}!')


def main():
    even_game(name)


if __name__ == '__main__':
    main()

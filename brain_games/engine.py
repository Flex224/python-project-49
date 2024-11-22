import prompt


MAX_ROUNDS = 3


def start(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    for counter in range(1, MAX_ROUNDS + 1):
        question, correct_answer = game.make_game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let\'s try again, {name}!")
            break
        if counter == MAX_ROUNDS:
            print(f'Congratulations, {name}!')

from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(progression_len, min_step, max_step,
                     min_first_num, max_first_num):
    first_num = randint(min_first_num, max_first_num)
    progression_step = randint(min_step, max_step)
    progression = list(range(first_num,
                             first_num + progression_step * progression_len,
                             progression_step))
    return progression


def generate_expression():
    progression = generate_progression(progression_len=10, min_step=1, max_step=10,
                                   min_first_num=0, max_first_num=100)
    random_index = randint(0, len(progression) - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(str(num) for num in progression)
    return question, str(correct_answer)

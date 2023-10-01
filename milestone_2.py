import random
import string

# set up variables for game
word_list = ['grapes', 'orange', 'plum', 'kiwi', 'banana']

# print(f'Random word is {word}')
alphabet = string.ascii_lowercase


def generate_random_word(word_list):
    '''
    args: a list of words

    return: a word from that list
    '''
    return random.choice(word_list)


def get_input():
    guess = input('Please guess a single letter: ')
    return guess


def validate_input(guess):
    '''
    Args:
        guess: string, which should be one character and a alphabetical letter
    Return:
        True or False depending on whether it adheres to the conditions
    '''
    if len(guess) == 1 and guess.lower() in alphabet:
        print('Good guess!')
        return True
    else:
        print('Oops! That is not a valid input.')
        return False


def hangman():
    word = generate_random_word(word_list)
    guess = get_input()
    validate_input(guess)


hangman()

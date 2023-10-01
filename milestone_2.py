import random
import string

# set up variables for game
word_list = ['grapes', 'orange', 'plum', 'kiwi', 'banana']
# print(word_list)
word = random.choice(word_list)
# print(f'Random word is {word}')
alphabet = string.ascii_lowercase


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
    guess = get_input()
    validate_input(guess)


hangman()

import random
import string

word_list = ['grapes', 'orange', 'plum', 'kiwi', 'banana']
print(word_list)
word = random.choice(word_list)
print(f'Random word is {word}')

guess = input('Please guess a single letter: ')
alphabet = string.ascii_lowercase


if len(guess) == 1 and guess.lower() in alphabet:
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')

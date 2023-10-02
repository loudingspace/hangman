import random

word_list = ['grapes', 'orange', 'plum', 'kiwi', 'banana']


def generate_random_word(word_list):
    '''
    args: a list of words

    return: a word from that list
    '''
    return random.choice(word_list)


word = generate_random_word(word_list)
print(word)

while True:
    guess = input('Please guess a single letter: ')
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')


if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")

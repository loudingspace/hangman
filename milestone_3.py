import milestone_2

while True:
    guess = input('Please guess a single letter: ')
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')

# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

In the program, we have a class Hangman with two methods, check_guess(guess) and ask_for_input(), and an **init** that takes two arguments, a word list and a number for number of lives (the second of these is optional).

We instantiate the class Hangman by passing it a word list. This will choose a random word from the word_list and assign it as an attribute of the object. It also creates an attribute with a representation of the guessed letters, the number of unique letters in the word, a list of the guesses already made and the lives left.

In the code, once you have instantiated the object we need to call the method ask_for_input() on the object to run the game engine as it stands.

To run use python:

    python milestone_4.py

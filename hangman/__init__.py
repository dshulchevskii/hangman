from random import choice
from .game import Hangman


PUZZLE_WORDS = ['hello', 'world', 'python', 'ruby']


def play_hangman():
    word = choice(PUZZLE_WORDS)
    play = Hangman(word)
    play.run()

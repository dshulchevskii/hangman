import hangman.game


def input_capture(word):
    letters = list(reversed(word))

    def func():
        char = letters.pop()
        print(char)
        return char
    return func


WIN_LOG = """
Guess a letter:
a
Missed, mistake 1 out of 5.

The word: *****

Guess a letter:
b
Missed, mistake 2 out of 5.

The word: *****

Guess a letter:
e
Hit!

The word: *e***

Guess a letter:
o
Hit!

The word: *e**o

Guess a letter:
l
Hit!

The word: *ello

Guess a letter:
h
Hit!

The word: hello

You won!
"""

LOSE_LOG = """
Guess a letter:
x
Missed, mistake 1 out of 5.

The word: ******

Guess a letter:
y
Missed, mistake 2 out of 5.

The word: ******

Guess a letter:
z
Missed, mistake 3 out of 5.

The word: ******

Guess a letter:
n
Hit!

The word: **n*n*

Guess a letter:
m
Missed, mistake 4 out of 5.

The word: **n*n*

Guess a letter:
o
Missed, mistake 5 out of 5.

The word: **n*n*

You lost!
"""


def test_win_run_game(capfd):
    game_session = hangman.game.Hangman('hello')
    hangman.game.input = input_capture('abeolh')
    game_session.run()
    out, _ = capfd.readouterr()
    assert out == WIN_LOG


def test_lose_run_game(capfd):
    game_session = hangman.game.Hangman('wining')
    hangman.game.input = input_capture('xyznmo')
    game_session.run()
    out, _ = capfd.readouterr()
    assert out == LOSE_LOG

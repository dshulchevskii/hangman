class Hangman():
    max_mistakes = 5

    def __init__(self, word):
        self.word = word
        self.mistakes = 0
        self.letters = []

    def open_word(self):
        return ''.join(l if l in self.letters else '*' for l in self.word)

    def step(self):
        print()
        print('Guess a letter:')
        letter = str(input())
        self.letters.append(letter)
        if letter in self.word:
            print('Hit!')
        else:
            self.mistakes += 1
            print('Missed, mistake %d out of %d.' % (self.mistakes,
                                                     self.max_mistakes))
        print()
        print("The word: %s" % self.open_word())

    def run(self):
        while self.mistakes < self.max_mistakes:
            self.step()
            if self.open_word() == self.word:
                print('\nYou won!')
                return
        print('\nYou lost!')

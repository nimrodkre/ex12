import itertools

WORDS_FILE = "boggle_dict.txt"


class Boogle:
    def __init__(self, words):
        self.__words = words

    @property
    def words(self):
        return self.__words

    @words.setter
    def words(self, words):
        self.__words = words

    def words_found(self, letters):
        return [word if word in self.words else None for word in
                itertools.combinations(letters, len(letters))]


def load_words():
    with open(WORDS_FILE, 'r') as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    print(len(load_words()))

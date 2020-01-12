import itertools


class BoardBL:
    def __init__(self, words):
        self.__words = words

    @property
    def words(self):
        return self.__words

    @words.setter
    def words(self, words):
        self.__words = words

    def check_word(self, letters):
        """
        receives word and checks if the given word was found in the words
        :param letters: the letters to check
        :return: score to give if the word is good, else -1
        """
        if letters in self.words:
            return len(letters) ** 2
        return -1




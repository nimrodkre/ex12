
class BoardBL:
    def __init__(self, words, board):
        self.__words = words
        self.__board = board

    @property
    def words(self):
        return self.__words

    @property
    def board(self):
        return self.__board

    def check_word(self, letters):
        """
        receives word and checks if the given word was found in the words
        :param letters: the letters to check
        :return: score to give if the word is good, else -1
        """
        if letters in self.__words:
            return len(letters) ** 2
        return -1

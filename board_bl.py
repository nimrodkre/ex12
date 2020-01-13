
class BoardBL:
    def __init__(self, board, words,):
        self.__board = board
        self.__words = words

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

    def is_letter_valid(self, i, j, prev_i, prev_j):
        if prev_i == -1 or prev_j == -1:
            return True

        if prev_i == i and prev_j == j:
            return False

        return prev_i - 1 <= i <= prev_i + 1 and prev_j - 1 <= j <= prev_j + 1

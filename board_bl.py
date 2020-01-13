
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
        if letters in self.words:
            return len(letters) ** 2
        return -1

    def is_letter_valid(self, row, col, prev_row, prev_col):
        if prev_col == -1 or prev_row == -1:
            return True
        if row == prev_row and col == prev_col:
            return False
        return (prev_row + 1 >= row >= prev_row - 1
                and prev_col + 1 >= col >= prev_col - 1)

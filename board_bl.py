
class BoardBL:
    def __init__(self, board, words):
        self.__board = board
        self.__words = words
        self.__guessed_words = set()
        self.__score = 0

    @property
    def words(self):
        return self.__words

    @property
    def board(self):
        return self.__board

    @property
    def score(self):
        return self.__score

    @property
    def guessed_words(self):
        return list(sorted(self.__guessed_words))

    def guess_word(self, word):
        """
        receives word and checks if the given word was found in the words
        :param word: the letters to check
        :return: score to give if the word is good, else -1
        """
        if word in self.__guessed_words:
            return False
        if word.lower() in self.__words:
            self.__guessed_words.add(word)
            self.__score += len(word) ** 2
            return True
        return False

    def is_letter_valid(self, i, j, prev_i, prev_j):
        if prev_i == -1 or prev_j == -1:
            return True

        if prev_i == i and prev_j == j:
            return False

        return prev_i - 1 <= i <= prev_i + 1 and prev_j - 1 <= j <= prev_j + 1

    def get_letter(self, i, j):
        return self.__board[i][j]

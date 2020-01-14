import datetime
import boggle_board_randomizer

INITIAL_TIME = 10


class BoardBL:
    def __init__(self, words):
        self.__board = boggle_board_randomizer.randomize_board()
        self.__words = words
        self.__guessed_words = set()
        self.__score = 0
        self.__time = datetime.timedelta(seconds=INITIAL_TIME)
        self.__times_up = None

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

    @property
    def time(self):
        return self.__time

    def decrease_time(self):
        if self.__time.seconds > 0:
            self.__time -= datetime.timedelta(seconds=1)
            if self.is_time_up() and self.__times_up is not None:
                self.__times_up()

    def is_time_up(self):
        return self.__time.total_seconds() == 0

    def guess_word(self, word):
        """
        receives word and checks if the given word was found in the words
        :param word: the letters to check
        :return: score to give if the word is good, else -1
        """
        if word == '':
            return 'Come on, you can do better!'
        if word in self.__guessed_words:
            return 'Already guessed!'
        if word.upper() in self.__words:
            self.__guessed_words.add(word)
            self.__score += len(word) ** 2
            return None
        return '{}? That\'s not a real word...'.format(word)

    def is_letter_valid(self, i, j, prev_i, prev_j):
        if prev_i == -1 or prev_j == -1:
            return True

        if prev_i == i and prev_j == j:
            return False

        return prev_i - 1 <= i <= prev_i + 1 and prev_j - 1 <= j <= prev_j + 1

    def get_letter(self, i, j):
        return self.__board[i][j]

    def restart_game(self):
        self.__guessed_words = set()
        self.__score = 0
        self.__time = datetime.timedelta(seconds=INITIAL_TIME + 1)
        self.__board = boggle_board_randomizer.randomize_board()

    def times_up_sub(self, action):
        self.__times_up = action

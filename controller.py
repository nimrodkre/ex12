from board_bl import BoardBL


class Controller:
    def __init__(self, board_bl: BoardBL):
        self.__board_bl = board_bl

    @property
    def board(self):
        return self.__board_bl.board

    @property
    def score(self):
        return self.__board_bl.score

    @property
    def time(self):
        return self.__board_bl.time

    def decrease_time(self):
        self.__board_bl.decrease_time()

    def guess_word(self, word):
        return self.__board_bl.guess_word(word)

    def is_letter_valid(self, row, col, prev_row, prev_col):
        return self.__board_bl.is_letter_valid(row, col, prev_row, prev_col)

    def get_letter(self, i, j):
        return self.__board_bl.get_letter(i, j)

    def is_time_up(self):
        return self.__board_bl.is_time_up()

    @property
    def guessed_words(self):
        return self.__board_bl.guessed_words

    def quit_game(self):
        pass

    def restart_game(self):
        self.__board_bl.restart_game()

    def times_up_sub(self, action):
        self.__board_bl.times_up_sub(action)

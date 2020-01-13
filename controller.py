class Controller:
    def __init__(self, board_bl):
        self.__board_bl = board_bl

    @property
    def board(self):
        return self.__board_bl.board

    def guess_word(self):
        return self.__board_bl.check_word()

    def is_letter_valid(self, row, col, prev_row, prev_col):
        return self.is_letter_valid(row, col, prev_row, prev_col)

    def quit_game(self):
        pass

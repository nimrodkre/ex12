class Collaborator:
    def __init__(self, board_bl, board_ui):
        self.__board_bl = board_bl

    @property
    def board_bl(self):
        return self.__board_bl

    @property
    def board_ui(self):
        return self.__board_ui

    @board_bl.setter
    def board_bl(self, board_bl):
        self.__board_bl = board_bl

    def guess_word(self):
        pass

    def quit_game(self):
        pass

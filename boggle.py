from board_bl import BoardBL
from board_ui import BoardUI
from controller import Controller

WORDS_FILE = "boggle_dict.txt"


class BoggleGameManager:
    def __init__(self, words):
        self.__words = words
        self.__ui = None
        self.__boggle_bl = None

    def start_game(self):
        self.__boggle_bl = BoardBL(self.__words)
        controller = Controller(self.__boggle_bl)
        self.__ui = BoardUI(controller)
        self.__ui.build_ui()
        self.__ui.root.mainloop()


def load_words():
    with open(WORDS_FILE, 'r') as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    words = load_words()
    boggle_manager = BoggleGameManager(words)
    boggle_manager.start_game()

import boggle_board_randomizer
from board_bl import BoardBL
from board_ui import BoardUI
from controller import Controller

WORDS_FILE = "boggle_dict.txt"


class BoggleGameManager:
    def __init__(self, words):
        self.__words = words

    def start_game(self):
        board = boggle_board_randomizer.randomize_board()
        boggle_bl = BoardBL(board, self.__words)
        controller = Controller(boggle_bl)
        a = BoardUI(controller)
        a.root.mainloop()


def load_words():
    with open(WORDS_FILE, 'r') as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    print(len(load_words()))
    words = load_words()
    boggle_manager = BoggleGameManager(words)
    boggle_manager.start_game()

import tkinter


class BoardUI:

    def __init__(self, board):
        self.__board = board
        self.__canvas = tkinter.Canvas()
        self.__buttons = []
        self.__score = None
        self.__quit = None
        self.__start = None
        self.__guess = None
        self.__screen = tkinter.Tk()

    @property
    def board(self):
        return self.__board

    @property
    def buttons(self):
        return self.__buttons

    @property
    def screen(self):
        return self.__screen

    @property
    def score(self):
        return self.__score

    @property
    def quit(self):
        return self.__quit

    @property
    def start(self):
        return self.__start

    @property
    def guess(self):
        return self.__guess

    @property
    def canvas(self):
        return self.__canvas

    @board.setter
    def board(self, board):
        self.__board = board

    @buttons.setter
    def buttons(self, buttons):
        self.__buttons = buttons

    @screen.setter
    def screen(self, screen):
        self.__screen = screen

    @quit.setter
    def quit(self, quit):
        self.__quit = quit

    @guess.setter
    def guess(self, guess):
        self.__guess = guess

    @start.setter
    def start(self, start):
        self.__start = start

    @score.setter
    def score(self, score):
        self.__score = score

    @canvas.setter
    def canvas(self, canvas):
        self.__score = canvas

    def build_board(self):
        pass

    def build_score_box(self):
        pass

    def build
import tkinter


class BoardUI:

    def __init__(self, board):
        self.__board = board
        self.__canvas = tkinter.Canvas()
        self.__buttons = []
        self.__score = 0
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

    @score.setter
    def score(self, score):
        self.__score = score

    @canvas.setter
    def canvas(self, canvas):
        self.__score = canvas

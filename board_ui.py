import tkinter
import ttk

class BoardUI:

    def __init__(self, board):
        self.__board = board
        self.__buttons = []
        self.__canvas = tkinter.Canvas()

    @property
    def board(self):
        return self.__board

    @property
    def buttons(self):
        return self.__buttons

    @board.setter
    def board(self, board):
        self.__board = board

    @buttons.setter
    def buttons(self, buttons):
        self.__buttons = buttons
        

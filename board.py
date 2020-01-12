import tkinter
import itertools

class Board:

    def __init__(self):
        self.__buttons = []
        self.__score = 0
        self.__screen = tkinter.Tk()

    @property
    def screen(self):
        return self.__screen

    @property
    def buttons(self):
        return self.__buttons

    @buttons.setter
    def buttons(self, buttons):
        self.__buttons = buttons

    @screen.setter
    def screen(self, screen):
        self.__screen = screen

    @staticmethod
    def callback():

    def build_buttons(self):
        pass


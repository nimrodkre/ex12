import tkinter


class BoardUI:

    def __init__(self, board):
        self.__board = board
        self.__root = tkinter.Tk()
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
    def root(self):
        return self.__root

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

    @root.setter
    def root(self, root):
        self.__score = root

    def __button_callback(self, i, j):
        # for some reason not working
        pass

    def build_buttons(self):
        for i in range(len(self.board)):
            self.buttons.append([tkinter.Button(self.root,
                                                text=self.board[i][j],
                                                command=lambda: self.__button_callback(
                                                    i, j)) for j in
                                 range(len(self.board[0]))])
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[0])):
                self.buttons[i][j].grid(row=i + 1, column=j + 1)

    def build_score(self):
        self.score = tkinter.Text(self.root, height=1, width=10)
        self.score.insert(tkinter.INSERT, "Score=0")
        self.score.grid(row=0, column=0)


a = BoardUI([['a', 'b'], ['g', 'j']])
a.build_score()
a.build_buttons()
a.root.mainloop()

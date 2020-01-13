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
        self.__current_word = None
        self.__undo = None
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
    def current_word(self):
        return self.__current_word

    @property
    def undo(self):
        return self.__undo

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

    @current_word.setter
    def current_word(self, current_word):
        self.__current_word = current_word

    @undo.setter
    def undo(self, undo):
        self.__undo = undo

    @root.setter
    def root(self, root):
        self.__score = root

    def __button_callback(self, i, j):
        # for some reason not working
        print(i, j)

    def make_callback(self, i, j):
        return lambda: self.__button_callback(i, j)

    def build_buttons(self):
        for i in range(len(self.board)):
            self.buttons.append([tkinter.Button(self.root,
                                                text=self.board[i][j],
                                                height=1, width=7,
                                                command=self.make_callback(i,
                                                                           j))
                                 for j in
                                 range(len(self.board[0]))])
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[0])):
                self.buttons[i][j].grid(row=i + 1, column=j)

    def build_score(self):
        self.score = tkinter.Text(self.root, height=1, width=10)
        self.score.insert(tkinter.INSERT, "Score=0")
        self.score.grid(row=0, column=0, columnspan=4)

    def build_current_word(self):
        pass

    def build_quit(self):
        pass

    def build_quess(self):
        pass

    def build_undo(self):
        pass


a = BoardUI([['a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a']])
a.build_score()
a.build_buttons()
a.root.mainloop()

import tkinter
import math

CURRENT_LETTERS_ROW = 0
CURRENT_LETTERS_COL = 2
CURRENT_LETTERS_COLSPAN = 3
GUESS_ROW = 0
GUESS_COL = 0
WORDS_ROW = 1
WORDS_COL = 0
WORDS_ROWSPAN = 3
SCORE_ROW = 4
SCORE_COL = 0
BUTTONS_START_ROW = 1
BUTTONS_START_COL = 1
UNDO_ROW = 0
UNDO_COL = 1
QUIT_ROW = 5
QUIT_COL = 0
TIMER_ROW = 5
TIMER_COL = 2
TIMER_COLSPAN = 3


class BoardUI:
    button_coordinates = {}

    def __init__(self, board):
        self.__board = board
        self.__root = tkinter.Tk()
        self.__buttons = []
        self.__score = None
        self.__quit = None
        self.__start = None
        self.__guess = None
        self.__current_word = None
        self.__words_guessed = None
        self.__timer = None
        self.__undo = None
        self.__screen = tkinter.Tk()

        self.__pressed_buttons = []

    def build_game(self):
        self.build_score()
        self.build_buttons()
        self.build_current_word()
        self.build_quit()
        self.build_guess()
        self.build_undo()
        self.build_words_guessed()
        self.root.mainloop()

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
    def words_guessed(self):
        return self.__words_guessed

    @property
    def timer(self):
        return self.__timer

    @property
    def root(self):
        return self.__root

    @property
    def pressed_buttons(self):
        return self.__pressed_buttons

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

    @words_guessed.setter
    def words_guessed(self, words_guessed):
        self.__words_guessed = words_guessed

    @timer.setter
    def timer(self, timer):
        self.__timer = timer

    @pressed_buttons.setter
    def pressed_buttons(self, pressed_buttons):
        self.__pressed_buttons = pressed_buttons

    @root.setter
    def root(self, root):
        self.__score = root

    def __button_callback(self, i, j):
        """
        Add text to current word, enable allowed buttons, and disable
        not allowed buttons.
        :param i: the location of the button pressed
        :param j: the location of the button pressed
        :return: None
        """
        self.current_word.configure(state='normal')
        self.current_word.insert(tkinter.INSERT, self.buttons[i][j]['text'])
        self.current_word.configure(state='disabled')
        self.__disable_buttons(i, j)
        self.__enable_buttons(i, j)
        self.pressed_buttons.append(self.buttons[i][j])

    def __disable_buttons(self, row, col):
        """
        disable all buttons not touching our button
        :param row: row
        :param col: col
        :return: None
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if math.fabs(i - row) > 1 or math.fabs(j - col) > 1:
                    self.buttons[i][j]['state'] = 'disabled'
        self.buttons[row][col]['state'] = 'disabled'

    def __enable_buttons(self, row, col):
        """
        enables the buttons around this button
        :param row:
        :param col:
        :return:
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if not (math.fabs(i - row) > 1 or math.fabs(j - col) > 1) and \
                        self.buttons[i][j] not in self.pressed_buttons and not(
                        i == row and j == col):
                    self.buttons[i][j]['state'] = 'normal'

    def make_callback(self, i, j):
        return lambda: self.__button_callback(i, j)

    def build_buttons(self):
        for i in range(len(self.board)):
            self.buttons.append([tkinter.Button(self.root,
                                                text=self.board[i][j],
                                                height=3, width=7,
                                                command=self.make_callback(i,
                                                                           j),
                                                padx=10)
                                 for j in
                                 range(len(self.board[0]))])
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[0])):
                BoardUI.button_coordinates[self.buttons[i][j]] = (i, j)
                self.buttons[i][j].grid(row=i + BUTTONS_START_ROW,
                                        column=j + BUTTONS_START_COL)

    def build_score(self):
        self.score = tkinter.Text(self.root, height=3, width=14, bg="gray")
        self.score.insert(tkinter.INSERT, "Score=0")
        self.score.configure(state='disabled')
        self.score.grid(row=SCORE_ROW, column=SCORE_COL)

    def build_current_word(self):
        self.current_word = tkinter.Text(self.root, height=1.3, width=30,
                                         bg="gray")
        self.current_word.insert(tkinter.INSERT, "letters:")
        self.current_word.configure(state='disabled')
        self.current_word.grid(row=CURRENT_LETTERS_ROW,
                               column=CURRENT_LETTERS_COL,
                               columnspan=CURRENT_LETTERS_COLSPAN)

    def build_quit(self):
        self.quit = tkinter.Button(text="QUIT", height=1, width=15, bg="red")
        self.quit.grid(row=QUIT_ROW, column=QUIT_COL)

    def build_guess(self):
        self.guess = tkinter.Button(text="GUESS", height=1, width=15)
        self.guess.grid(row=GUESS_ROW, column=GUESS_COL)

    def __del_last_letter(self):
        self.current_word.configure(state='normal')
        word = self.current_word.get("1.0", 'end')
        new_word = word[:len(word) - 2]
        self.current_word.delete("1.0", "end")
        self.current_word.insert("1.0", new_word)
        self.current_word.configure(state='disabled')

    def __undo_button(self, button):
        if len(self.pressed_buttons) == 0:
            for i in range(len(self.buttons)):
                for j in range(len(self.buttons[0])):
                    self.buttons[i][j]['state'] = 'normal'
            return
        loc = BoardUI.button_coordinates[self.pressed_buttons[-1]]
        self.__disable_buttons(*loc)
        self.__enable_buttons(*loc)

    def __undo_callback(self):
        print(len(self.pressed_buttons))
        if len(self.pressed_buttons) == 0:
            return
        self.__del_last_letter()
        self.__undo_button(self.pressed_buttons.pop())


    def build_undo(self):
        self.undo = tkinter.Button(text="UNDO", height=1, width=10, command=self.__undo_callback)
        self.undo.grid(row=UNDO_ROW, column=UNDO_COL)

    def build_words_guessed(self):
        self.words_guessed = tkinter.Text(self.root, height=10, width=14,
                                          bg="gray")
        self.words_guessed.insert(tkinter.INSERT, "WORDS")
        self.words_guessed.configure(state='disabled')
        self.words_guessed.grid(row=WORDS_ROW,
                                column=WORDS_COL,
                                rowspan=WORDS_ROWSPAN)

    def build_timer(self):
        pass


a = BoardUI([['a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a']])
a.build_game()


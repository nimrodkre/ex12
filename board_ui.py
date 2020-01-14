import tkinter
from tkinter import DISABLED, NORMAL
from controller import Controller
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
TIMER_COL = 1
TIMER_COLSPAN = 1
MSG_LBL_ROW = 6
MSG_LBL_COL = 2
MSG_LBL_COLSPAN = 3
START_BTN_ROW = 5
START_BTN_COL = 4


class BoardUI:
    button_coordinates = {}

    def __init__(self, controller: Controller):
        self.__controller = controller
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
        self.__pressed_buttons = []
        self.__msg_lbl = None

        self.__prev_i = -1
        self.__prev_j = -1
        self.__guessed_word = ''
        self.__controller.times_up_sub(self.__end_game)
        self.__root.title('Crazy Boggle')

    @property
    def buttons(self):
        return self.__buttons

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

    @buttons.setter
    def buttons(self, buttons):
        self.__buttons = buttons

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
        self.__guessed_word += self.buttons[i][j]['text']
        self.current_word.config(text='Letters: ' + self.__guessed_word)
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
        for i in range(len(self.__controller.board)):
            for j in range(len(self.__controller.board[0])):
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
        for i in range(len(self.__controller.board)):
            for j in range(len(self.__controller.board[0])):
                if not (math.fabs(i - row) > 1 or math.fabs(j - col) > 1) and \
                        self.buttons[i][
                            j] not in self.pressed_buttons and not (
                        i == row and j == col):
                    self.buttons[i][j]['state'] = 'normal'

    def make_callback(self, i, j):
        return lambda: self.__button_callback(i, j)

    def build_buttons(self):
        for i in range(len(self.__controller.board)):
            self.buttons.append([tkinter.Button(self.root,
                                                text='X'
                                                , height=3, width=7,
                                                command=self.make_callback(i,
                                                                           j),
                                                padx=10, state=DISABLED)
                                 for j in
                                 range(len(self.__controller.board[0]))])
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[0])):
                BoardUI.button_coordinates[self.buttons[i][j]] = (i, j)
                self.buttons[i][j].grid(row=i + BUTTONS_START_ROW,
                                        column=j + BUTTONS_START_COL)

    def build_score(self):
        self.score = tkinter.Label(self.root, height=3, width=14, bg="gray",
                                      text="Score=0")
        self.score.grid(row=SCORE_ROW, column=SCORE_COL)

    def build_current_word(self):
        self.current_word = tkinter.Label(self.root, height=1, width=30,
                                          bg="gray", text="letters:", anchor='w')
        self.current_word.grid(row=CURRENT_LETTERS_ROW,
                               column=CURRENT_LETTERS_COL,
                               columnspan=CURRENT_LETTERS_COLSPAN)

    def build_quit(self):
        self.__quit = tkinter.Button(text="QUIT", height=1, width=15,
                                       bg="red",
                                       command=quit)
        self.__quit.grid(row=QUIT_ROW, column=QUIT_COL)

    def build_guess(self):
        self.__guess = tkinter.Button(text="GUESS", height=1, width=15,
                                        command=self.__guess_word)
        self.__guess.grid(row=GUESS_ROW, column=GUESS_COL)

    def __del_last_letter(self):
        self.__guessed_word = self.__guessed_word[:-1]
        self.current_word.config(text='Letters: ' + self.__guessed_word)

    def __undo_button(self):
        if len(self.pressed_buttons) == 0:
            for i in range(len(self.buttons)):
                for j in range(len(self.buttons[0])):
                    self.buttons[i][j]['state'] = 'normal'
            return
        loc = BoardUI.button_coordinates[self.pressed_buttons[-1]]
        self.__disable_buttons(*loc)
        self.__enable_buttons(*loc)

    def __undo_callback(self):
        if len(self.pressed_buttons) == 0:
            return
        self.__del_last_letter()
        self.__undo_button()

    def build_undo(self):
        self.undo = tkinter.Button(text="UNDO", height=1, width=10,
                                   command=self.__undo_callback)
        self.undo.grid(row=UNDO_ROW, column=UNDO_COL)

    def build_words_guessed(self):
        self.words_guessed = tkinter.Label(self.root, height=10, width=14,
                                           bg="gray", text="WORDS", anchor='n')
        self.words_guessed.grid(row=WORDS_ROW,
                                column=WORDS_COL,
                                rowspan=WORDS_ROWSPAN)

    def build_timer(self):
        self.__timer = tkinter.Label(self.root, height=1, width=10,
                                     text=str(self.__controller.time)[2:])
        self.__timer.grid(row=TIMER_ROW,
                          column=TIMER_COL,
                          rowspan=TIMER_COLSPAN)

    def build_start(self):
        self.start = tkinter.Button(text="START", height=1, width=10,
                                    command=self.__start_game)
        self.start.grid(row=START_BTN_ROW, column=START_BTN_COL)

    def build_msg_label(self):
        self.__msg_lbl = tkinter.Label(text='', anchor='w')
        self.__msg_lbl.grid(row=MSG_LBL_ROW, column=MSG_LBL_COL, columnspan=MSG_LBL_COLSPAN)

    def __update_timer(self):
        self.__controller.decrease_time()
        self.__timer.config(text=str(self.__controller.time)[2:])
        if not self.__controller.is_time_up():
            self.root.after(1000, self.__update_timer)

    def build_ui(self):
        self.build_score()
        self.build_buttons()
        self.build_current_word()
        self.build_quit()
        self.build_guess()
        self.build_undo()
        self.build_words_guessed()
        self.build_start()
        self.build_timer()
        self.build_msg_label()

    def __guess_word(self):
        guess_word_msg = self.__controller.guess_word(self.__guessed_word)
        if guess_word_msg is None:
            guessed_words = 'WORDS\n' + '\n'.join(
                self.__controller.guessed_words)
            self.words_guessed.config(text=guessed_words)
            guess_word_msg = 'Nice one!'
        self.score.config(text='Score=' + str(self.__controller.score))
        self.__prev_i = -1
        self.__prev_j = -1
        self.__guessed_word = ''
        self.current_word.config(text='Letters: ' + self.__guessed_word)
        self.__msg_lbl.config(text=guess_word_msg)

        self.__pressed_buttons = []
        for row in self.__buttons:
            for btn in row:
                btn.config(state=NORMAL)

    def __start_game(self):
        self.__update_timer()
        self.__pressed_buttons = []
        self.start.config(text='START', command=self.__restart_game,
                          state=DISABLED)
        for i, btn_row in enumerate(self.buttons):
            for j, btn in enumerate(btn_row):
                btn.config(text=self.__controller.get_letter(i, j),
                           state=NORMAL)

    def __end_game(self):
        self.start.config(text='RESTART', command=self.__restart_game,
                          state=NORMAL)
        self.__msg_lbl.config(text='Times Up!')
        for i, btn_row in enumerate(self.buttons):
            for j, btn in enumerate(btn_row):
                btn.config(state=DISABLED)

    def __restart_game(self):
        self.__controller.restart_game()
        self.__start_game()
        self.__msg_lbl.config(text='')

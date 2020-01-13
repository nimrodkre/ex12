import tkinter
from tkinter import DISABLED, NORMAL
from controller import Controller

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

    def __init__(self, controller: Controller):
        self.__controller = controller
        self.__root = tkinter.Tk()
        self.__buttons = []
        self.__score_tb = None
        self.__quit_btn = None
        self.__start = None
        self.__guess_btn = None
        self.__current_word = None
        self.__words_guessed_tb = None
        self.__timer = None
        self.__undo = None

        self.__prev_i = -1
        self.__prev_j = -1
        self.__guess = ''
        self.__controller.times_up_sub(self.__end_game)
        self.__root.title('Crazy Boggle')

    @property
    def buttons(self):
        return self.__buttons

    @property
    def score_tb(self):
        return self.__score_tb

    @property
    def quit_btn(self):
        return self.__quit_btn

    @property
    def start(self):
        return self.__start

    @property
    def guess_btn(self):
        return self.__guess_btn

    @property
    def current_word(self):
        return self.__current_word

    @property
    def undo(self):
        return self.__undo

    @property
    def words_guessed(self):
        return self.__words_guessed_tb

    @property
    def timer(self):
        return self.__timer

    @property
    def root(self):
        return self.__root

    @buttons.setter
    def buttons(self, buttons):
        self.__buttons = buttons

    @quit_btn.setter
    def quit_btn(self, quit_btn):
        self.__quit_btn = quit_btn

    @guess_btn.setter
    def guess_btn(self, guess):
        self.__guess_btn = guess

    @start.setter
    def start(self, start):
        self.__start = start

    @score_tb.setter
    def score_tb(self, score):
        self.__score_tb = score

    @current_word.setter
    def current_word(self, current_word):
        self.__current_word = current_word

    @undo.setter
    def undo(self, undo):
        self.__undo = undo

    @words_guessed.setter
    def words_guessed(self, words_guessed):
        self.__words_guessed_tb = words_guessed

    @timer.setter
    def timer(self, timer):
        self.__timer = timer

    @root.setter
    def root(self, root):
        self.__score_tb = root

    def __button_callback(self, i, j):
        # for some reason not working
        if not self.__controller.is_letter_valid(i, j, self.__prev_i,
                                                 self.__prev_j):
            print('Not valid!!!')
            return
        self.__guess += self.__controller.get_letter(i, j)
        self.current_word.configure(text='Letters: ' + self.__guess)
        self.__prev_i = i
        self.__prev_j = j

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
                self.buttons[i][j].grid(row=i + BUTTONS_START_ROW,
                                        column=j + BUTTONS_START_COL)

    def build_score(self):
        self.score_tb = tkinter.Label(self.root, height=3, width=14, bg="gray",
                                      text="Score=0")
        self.score_tb.grid(row=SCORE_ROW, column=SCORE_COL)

    def build_current_word(self):
        self.current_word = tkinter.Label(self.root, height=1, width=30,
                                          bg="gray", text="letters:")
        self.current_word.grid(row=CURRENT_LETTERS_ROW,
                               column=CURRENT_LETTERS_COL,
                               columnspan=CURRENT_LETTERS_COLSPAN)

    def build_quit(self):
        self.quit_btn = tkinter.Button(text="QUIT", height=1, width=15,
                                       bg="red",
                                       command=quit)
        self.quit_btn.grid(row=QUIT_ROW, column=QUIT_COL)

    def build_guess(self):
        self.guess_btn = tkinter.Button(text="GUESS", height=1, width=15,
                                        command=self.__guess_word)
        self.guess_btn.grid(row=GUESS_ROW, column=GUESS_COL)

    def build_undo(self):
        self.undo = tkinter.Button(text="UNDO", height=1, width=10)
        self.undo.grid(row=UNDO_ROW, column=UNDO_COL)

    def build_words_guessed(self):
        self.words_guessed = tkinter.Label(self.root, height=10, width=14,
                                           bg="gray", text="WORDS")
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
        self.start.grid(row=BUTTONS_START_ROW, column=BUTTONS_START_COL)

    def build_msg_label(self):
        pass

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

    def __guess_word(self):
        if self.__controller.guess_word(self.__guess):
            guessed_words = 'WORDS\n' + '\n'.join(
                self.__controller.guessed_words)
            self.words_guessed.config(text=guessed_words)
        self.score_tb.config(text='Score=' + str(self.__controller.score))
        self.__prev_i = -1
        self.__prev_j = -1
        self.__guess = ''
        self.current_word.configure(text='Letters: ' + self.__guess)

    def __start_game(self):
        self.__update_timer()
        self.start.config(text='START', command=self.__restart_game,
                          state=DISABLED)
        for i, btn_row in enumerate(self.buttons):
            for j, btn in enumerate(btn_row):
                btn.config(text=self.__controller.get_letter(i, j),
                           state=NORMAL)

    def __end_game(self):
        self.start.config(text='RESTART', command=self.__restart_game,
                          state=NORMAL)
        print('Times UP!')

    def __restart_game(self):
        self.__controller.restart_game()
        self.__start_game()

import tkinter
from tkinter import DISABLED, NORMAL, ttk, INSERT, N, S, W, E, END
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
MSG_LBL_COL = 0
MSG_LBL_COLSPAN = 5
START_BTN_ROW = 5
START_BTN_COL = 4


class BoardUI:
    button_coordinates = {}

    def __init__(self, controller):
        """
        Creates a new UI component for the Boggle games
        :param controller: The games controller to activate the games logic
        """
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
        self.__scrollbar_list = None
        self.__pressed_buttons = []
        self.__msg_lbl = None
        self.__guessed_word = ''
        self.__controller.times_up_sub(self.__end_game)
        self.__root.title('Crazy Boggle')
        self.__root.configure(bg="azure")

        # Make the board non resizable
        self.__root.resizable(False, False)

    @property
    def root(self):
        """
        The root Tkinter object
        :return: A tkinter.Tk() that holds the UI of the game
        """
        return self.__root

    def build_ui(self):
        """
        Builds the game's UI window
        :return: None
        """
        self.__build_score()
        self.__build_buttons()
        self.__build_current_word()
        self.__build_quit()
        self.__build_guess()
        self.__build_undo()
        self.__build_words_guessed()
        self.__build_start()
        self.__build_timer()
        self.__build_msg_label()

    def __button_callback(self, i, j):
        """
        Add text to current word, enable allowed buttons, and disable
        not allowed buttons.
        :param i: the location of the button pressed
        :param j: the location of the button pressed
        :return: None
        """
        self.__guessed_word += self.__buttons[i][j]['text']
        self.__current_word.config(text='Letters: ' + self.__guessed_word)
        self.__disable_buttons(i, j)
        self.__enable_buttons(i, j)
        self.__pressed_buttons.append(self.__buttons[i][j])

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
                    self.__buttons[i][j].config(state=DISABLED)
        self.__buttons[row][col].config(state=DISABLED)

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
                        self.__buttons[i][
                            j] not in self.__pressed_buttons and not (
                        i == row and j == col):
                    self.__buttons[i][j].config(state=NORMAL)

    def __make_callback(self, i, j):
        """
        Makes the function for the button callback, in order for each paramete
        to be different
        :param i: coordinate row for the callback
        :param j: coordinate col
        :return: function of callback
        """
        return lambda: self.__button_callback(i, j)

    def __build_buttons(self):
        """
        builds all buttons on the screen
        :return:
        """
        for i in range(len(self.__controller.board)):
            self.__buttons.append([tkinter.Button(self.__root,
                                                  text='X'
                                                  , height=3, width=10,
                                                  command=self.__make_callback(
                                                      i,
                                                      j),
                                                  padx=10, state=DISABLED,
                                                  bg="turquoise")
                                   for j in
                                   range(len(self.__controller.board[0]))])
        # Add buttons to screen
        for i in range(len(self.__buttons)):
            for j in range(len(self.__buttons[0])):
                BoardUI.button_coordinates[self.__buttons[i][j]] = (i, j)
                self.__buttons[i][j].grid(row=i + BUTTONS_START_ROW,
                                          column=j + BUTTONS_START_COL)

    def __build_score(self):
        """
        builds score label
        :return: None
        """
        self.__score = tkinter.Label(self.__root, height=3, width=18,
                                     bg="light blue",
                                     text="Score=0")
        self.__score.grid(row=SCORE_ROW, column=SCORE_COL)

    def __build_current_word(self):
        """
        builds a label which holds the current letters chosen by the user
        :return:
        """
        self.__current_word = tkinter.Label(self.__root, height=1, width=39,
                                            bg="light blue", text="Letters:",
                                            anchor='w')
        self.__current_word.grid(row=CURRENT_LETTERS_ROW,
                                 column=CURRENT_LETTERS_COL,
                                 columnspan=CURRENT_LETTERS_COLSPAN)

    def __build_quit(self):
        """
        builds quit button
        :return:
        """
        self.__quit = tkinter.Button(text="QUIT", height=1, width=16,
                                     bg="salmon1",
                                     command=quit)
        self.__quit.grid(row=QUIT_ROW, column=QUIT_COL)

    def __build_guess(self):
        """
        builds guess button
        :return:
        """
        self.__guess = tkinter.Button(text="GUESS", height=1, width=16,
                                      command=self.__guess_word,
                                      state=DISABLED, bg="plum2")
        self.__guess.grid(row=GUESS_ROW, column=GUESS_COL)

    def __del_last_letter(self):
        """
        removes the last letter from the current guess, function used in undo
        :return:
        """
        # Qu always come together
        if self.__guessed_word.upper().endswith('QU'):
            self.__guessed_word = self.__guessed_word[:-2]
        else:
            self.__guessed_word = self.__guessed_word[:-1]
        self.__current_word.config(text='Letters: ' + self.__guessed_word)

    def __undo_button(self):
        """
        in charge of undoing the last steps.
        Uses stack to find out which was the last button clicked
        :return:
        """
        self.__pressed_buttons.pop()
        if len(self.__pressed_buttons) == 0:
            for i in range(len(self.__buttons)):
                for j in range(len(self.__buttons[0])):
                    self.__buttons[i][j].config(state=NORMAL)
            return
        loc = BoardUI.button_coordinates[self.__pressed_buttons[-1]]
        self.__disable_buttons(*loc)
        self.__enable_buttons(*loc)

    def __undo_callback(self):
        """
        in charge of what to do when undo is pressed
        :return:
        """
        if len(self.__pressed_buttons) == 0:
            return
        self.__del_last_letter()
        self.__undo_button()

    def __build_undo(self):
        """
        builds undo button
        :return:
        """
        self.__undo = tkinter.Button(text="UNDO", height=1, width=10,
                                     command=self.__undo_callback,
                                     state=DISABLED, bg="plum2")
        self.__undo.grid(row=UNDO_ROW, column=UNDO_COL)

    def __build_words_guessed(self):
        """
        builds a textbox with all words guessed.
        Also added scroll bar in order to allow more words to be put on the
        textbox.
        :return:
        """
        self.__words_guessed = tkinter.Text(self.__root, height=10, width=20,
                                            bg="light blue")
        self.__words_guessed.grid(row=WORDS_ROW,
                                  column=WORDS_COL,
                                  rowspan=WORDS_ROWSPAN)

        self.__words_guessed.tag_config('center', justify='center')
        self.__words_guessed.tag_add("center", "1.0", "end")

        self.__scrollbar_list = tkinter.Scrollbar(self.__root)

        self.__words_guessed.insert(INSERT, 'WORDS', 'center')
        self.__words_guessed.config(state=DISABLED)
        self.__scrollbar_list.grid(column=WORDS_COL, row=WORDS_ROW,
                                   rowspan=WORDS_ROWSPAN, sticky=N + S + E)

        # attach listbox to scrollbar
        self.__words_guessed.config(yscrollcommand=self.__scrollbar_list.set)
        self.__scrollbar_list.config(command=self.__words_guessed.yview)

    def __build_timer(self):
        """
        Builds a label containing the timer component
        :return: None
        """
        self.__timer = tkinter.Label(self.__root, height=1, width=12,
                                     text=str(self.__controller.time)[2:],
                                     bg="light blue")
        self.__timer.grid(row=TIMER_ROW,
                          column=TIMER_COL,
                          rowspan=TIMER_COLSPAN)

    def __build_start(self):
        """
        Build the start/restart button for the game
        :return: None
        """
        self.start = tkinter.Button(text="START", height=1, width=10,
                                    command=self.__start_game,
                                    bg="chartreuse2")
        self.start.grid(row=START_BTN_ROW, column=START_BTN_COL)

    def __build_msg_label(self):
        """
        Builds a label that holds an interactive message
        :return: None
        """
        self.__msg_lbl = tkinter.Label(text='', bg="azure")
        self.__msg_lbl.grid(row=MSG_LBL_ROW, column=MSG_LBL_COL,
                            columnspan=MSG_LBL_COLSPAN, sticky="NSEW")

    def __update_timer(self):
        """
        Updates the timer label every one second
        :return: None
        """
        self.__controller.decrease_time()
        # Take only the minutes and seconds from the timer
        self.__timer.config(text=str(self.__controller.time)[2:])

        # Keep updating every second as long as the time is not up
        if not self.__controller.is_time_up():
            self.__root.after(1000, self.__update_timer)

    def __guess_word(self):
        """
        Sends the user's guess to the game's logic
        :return: None
        """
        guess_word_msg = self.__controller.guess_word(self.__guessed_word)

        # Check if the user guessed correctly
        if guess_word_msg is None:
            guessed_words = 'WORDS\n' + '\n'.join(
                self.__controller.guessed_words)
            self.__words_guessed.config(state=NORMAL)
            self.__words_guessed.delete(1.0, END)
            self.__words_guessed.insert(INSERT, guessed_words, 'center')
            self.__words_guessed.config(state=DISABLED)
            guess_word_msg = 'Nice one!'

        self.__score.config(text='Score=' + str(self.__controller.score))
        self.__guessed_word = ''
        self.__current_word.config(text='Letters: ' + self.__guessed_word)
        self.__msg_lbl.config(text=guess_word_msg)

        self.__enable_all_buttons()

    def __enable_all_buttons(self):
        """
        Enables all the buttons on the board
        :return: None
        """
        self.__pressed_buttons = []
        for row in self.__buttons:
            for btn in row:
                btn.config(state=NORMAL)

    def __start_game(self):
        """
        resets all components of the game in order for us to start
        all over again
        :return:
        """
        self.__update_timer()
        self.__pressed_buttons = []
        self.__guessed_word = ''
        self.__current_word.config(text='Letters: ' + self.__guessed_word)
        self.__words_guessed.config(state=NORMAL)
        self.__words_guessed.delete(1.0, END)
        self.__words_guessed.insert(INSERT, 'WORDS', 'center')
        self.__words_guessed.config(state=DISABLED)
        self.__score.config(text='Score=' + str(self.__controller.score))
        self.start.config(text='START', command=self.__restart_game,
                          state=DISABLED)
        for i, btn_row in enumerate(self.__buttons):
            for j, btn in enumerate(btn_row):
                btn.config(text=self.__controller.get_letter(i, j),
                           state=NORMAL)
        self.__guess.config(state=NORMAL)
        self.__undo.config(state=NORMAL)

    def __end_game(self):
        """
        Ends the game
        :return: None
        """
        self.start.config(text='RESTART', command=self.__restart_game,
                          state=NORMAL)
        self.__msg_lbl.config(text='Times Up!')
        for i, btn_row in enumerate(self.__buttons):
            for j, btn in enumerate(btn_row):
                btn.config(state=DISABLED)
        self.__guess.config(state=DISABLED)
        self.__undo.config(state=DISABLED)

    def __restart_game(self):
        """
        Restarts the game with a brand new board
        :return: None
        """
        self.__controller.restart_game()
        self.__start_game()
        self.__msg_lbl.config(text='')

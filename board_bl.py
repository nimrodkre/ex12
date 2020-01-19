import datetime
import boggle_board_randomizer
import board_bl_codes

INITIAL_TIME = 180


class BoardBL:
    def __init__(self, words):
        """
        Creates a Boggle game logic component
        :param words: A list of valid English words
        """
        self.__board = boggle_board_randomizer.randomize_board()
        self.__words = words
        self.__guessed_words = set()
        self.__score = 0
        self.__time = datetime.timedelta(seconds=INITIAL_TIME)
        self.__times_up = None

    @property
    def board(self):
        """
        The current board of the game
        :return: A list of rows, each row is a list of letters in the current board
        """
        return self.__board

    @property
    def score(self):
        """
        The most current user's score
        :return: An integer representing the player's score
        """
        return self.__score

    @property
    def guessed_words(self):
        """
        A list of the words that the player has guessed so far
        :return: A list of strings
        """
        return list(sorted(self.__guessed_words))

    @property
    def time(self):
        """
        How much time left for the game
        :return: A datetime.timedelta object
        """
        return self.__time

    def decrease_time(self):
        """
        Decrease the time left for the game by one second
        :return: None
        """
        if self.__time.seconds > 0:
            self.__time -= datetime.timedelta(seconds=1)
            if self.is_time_up() and self.__times_up is not None:
                self.__times_up()

    def is_time_up(self):
        """
        Checks if the player's time is up
        :return: True if the no more time left, otherwise False
        """
        return self.__time.total_seconds() == 0

    def guess_word(self, word):
        """
        receives word and checks if the given word was found in the words
        :param word: the letters to check
        :return: score to give if the word is good, else -1
        """
        if word == '':
            return board_bl_codes.NO_GUESS
        if word in self.__guessed_words:
            return board_bl_codes.ALREADY_GUESSED

        if word.upper() in self.__words:
            self.__guessed_words.add(word)
            if 'QU' in word.upper():
                self.__score += (len(word) - 1) ** 2
            else:
                self.__score += len(word) ** 2
            return board_bl_codes.VALID_GUESS
        return board_bl_codes.NOT_A_WORD

    def get_letter(self, i, j):
        """
        Gets the letter on the board in the given coordinates
        :param i: The row index of the required letter
        :param j: The column index of the required letter
        :return: The letter in the required position
        """
        return self.__board[i][j]

    def restart_game(self):
        """
        Restarts a new Boggle game
        :return: None
        """
        self.__guessed_words = set()
        self.__score = 0
        self.__time = datetime.timedelta(seconds=INITIAL_TIME + 1)
        self.__board = boggle_board_randomizer.randomize_board()

    def times_up_sub(self, action):
        """
        Subscribe to the times_up event
        :param action: The action to invoke when the time is up
        :return: None
        """
        self.__times_up = action

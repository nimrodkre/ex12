from board_bl import BoardBL


class Controller:
    def __init__(self, board_bl: BoardBL):
        self.__board_bl = board_bl

    @property
    def board(self):
        """
        The current board of the game
        :return: A list of rows, each row is a list of letters in the current board
        """
        return self.__board_bl.board

    @property
    def score(self):
        """
        The most current user's score
        :return: An integer representing the player's score
        """
        return self.__board_bl.score

    @property
    def time(self):
        """
        How much time left for the game
        :return: A datetime.timedelta object
        """
        return self.__board_bl.time

    def decrease_time(self):
        """
        Decrease the time left for the game by one second
        :return: None
        """
        self.__board_bl.decrease_time()

    def is_time_up(self):
        """
        Checks if the player's time is up
        :return: True if the no more time left, otherwise False
        """
        return self.__board_bl.is_time_up()

    def guess_word(self, word):
        """
        receives word and checks if the given word was found in the words
        :param word: the letters to check
        :return: score to give if the word is good, else -1
        """
        return self.__board_bl.guess_word(word)

    @property
    def guessed_words(self):
        """
        A list of the words that the player has guessed so far
        :return: A list of strings
        """
        return self.__board_bl.guessed_words

    def get_letter(self, i, j):
        """
        Gets the letter on the board in the given coordinates
        :param i: The row index of the required letter
        :param j: The column index of the required letter
        :return: The letter in the required position
        """
        return self.__board_bl.get_letter(i, j)

    def restart_game(self):
        """
        Restarts a new Boggle game
        :return: None
        """
        self.__board_bl.restart_game()

    def times_up_sub(self, action):
        """
        Subscribe to the times_up event
        :param action: The action to invoke when the time is up
        :return: None
        """
        self.__board_bl.times_up_sub(action)

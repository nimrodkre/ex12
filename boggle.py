
WORDS_FILE = "boggle_dict.txt"


def load_words():
    with open(WORDS_FILE, 'r') as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    print(len(load_words()))

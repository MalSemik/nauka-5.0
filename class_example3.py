import random


class NonPersistentDictionary:
    def __init__(self):
        self.dict = {}

    def add_word(self, word, translation):
        self.dict[word] = translation

    def get_translation(self, word):
        if word in self.dict:
            return self.dict[word]


class DatabaseDictionary:
    """
    Some db magic here
    """


class TxtFileDictionary:
    def __init__(self, txt_file):
        self.txt_file = txt_file

    def add_word(self, word, translation):
        with open(self.txt_file, 'a') as my_dict:
            my_dict.write(word + " " + translation + '\n')

    def get_translation(self, word):
        with open(self.txt_file, 'r') as my_dict:
            content = my_dict.readlines()
            for line in content:
                word_from_file, transalation = line.split()
                if word_from_file == word:
                    return transalation


class Student:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def translate(self, word):
        translation = self.dictionary.get_translation(word)
        if translation is not None:
            print(f"Odpowiedz to {translation}")
        else:
            print("Nie znam tlumaczenia")


good_student = Student(TxtFileDictionary("zeszycik.txt"))
bad_student = Student(NonPersistentDictionary())


class TicTacToeGame:
    def __init__(self, player_one, player_two):
        pass


class ComputerPlayer:
    def choose_move(self, board):
        return random.randint()


class SmartComputerPlayer:
    def choose_move(self, board):
        print("Super advanced AI calculating next move")
        return random.randint(1, 10)


class HumanPlayer:
    pass

from api import WordTranslationGenerator
import random
import os
import pickle
import atexit


class WordCollection():

    def __init__(self,):
        self.__words = list()

    def add(self, word, translation):
        self.__words.append((word, translation))

    def add_random(self,):
        word, translation = WordTranslationGenerator.word_translation()
        self.add(word, translation)

    def translation_of(self, chosen_word):
        try:
            return next(
                pair[1]
                for pair in self.__words
                if pair[0] == chosen_word
            )
        except StopIteration:
            return None

    def get_last(self,):
        if not self.__words:
            return None
        return self.__words[-1]

    def get_random(self,):
        if not self.__words:
            return None
        return random.choice(self.__words)


class Database():

    def __init__(self, file_name):
        self.file_name = file_name
        self.data = self.__load()
        atexit.register(self.__save)

    def __load(self,):
        if os.path.isfile(self.file_name):
            with open(self.file_name, "rb") as file:
                return pickle.load(file)

        return WordCollection()

    def __save(self,):
        with open(self.file_name, "wb") as file:
            pickle.dump(self.data, file)


class Dictations():

    FILE = 'database.voc'

    def __init__(self,):
        self.data = Database(self.FILE)

    def print_last(self):
        """ Prints out the value of the last in json """

    def print_random(self,):
        """ prints random value """

    def print_list(self,):
        """ prints list of words and values """

    def dictation(self):
        """ prints last 15 values in saturday for dictation """

    def get_input(self, input):
        """ gets the input from the user to the dictation """

    def check_input(self,) -> bool:
        """ Checks input of user """

    def right(self):
        """ Prints if all answers are right """
        if self.check_input:
            print("You got it all right!")

    def wrong(self):
        """ Prints that you had mistakes in dictation """

    def try_again(self):
        """ Make a new try for the same dictatin """

    def where_mistake(self):
        """ prints where the mistakes are """

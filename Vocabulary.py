from api import WordTranslationGenerator
import random
import os
import pickle
import atexit

class WordCollection():
    
    def __init__(self,):
        self.__words = list()

    def add(self, word, translation):
        self.__words.append((word,translation))
    
    def add_random(self,):
        word,translation =  WordTranslationGenerator.word_translation()
        self.add(word, translation)
    
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

    def __load (self,):
        if os.path.isfile(self.file_name):
            with open (self.file_name, "rb") as file:
                return pickle.load(file)

        return WordCollection()
    
    def __save (self,): 
        with open (self.file_name, "wb") as file:
            pickle.dump(self.data, file)
        
    
    
    
class Dictations():
    def print_out(self):
        """ Prints out the value of the last in json """

    def dictation(self):
        """ prints last 15 values in saturday for dictation """
        

    def check_input (self):
        """ Checks input of user """


    def right(self):
        """ Prints if all answers are right """

    
    def wrong(self):
        """ Prints that you had mistakes in dictation """
        
    
    def try_again(self):
        """ Make a new try for the same dictatin """


    def where_mistake(self):
        """ prints where the mistakes are """












    


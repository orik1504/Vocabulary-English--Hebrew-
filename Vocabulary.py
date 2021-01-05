import json
import datetime
from bidi.algorithm import get_display 
from selenium import webdriver
import atexit
from bs4 import BeautifulSoup
import requests
import spellchecker

class Vocabulary():
    
    def __init__(self, json_path):
        self.__json_path = json_path
    
    def add_to_database(self,word, translation):
        with open(self.__json_path) as f:
            data = json.load(f)
        data[word] = translation
        with open(self.__json_path, 'w', encoding='utf8') as f:
            json.dump(data, f, indent=4)

    def print_out(self):
    """ Prints out the value of the last in json """

    def dictation(self):
    """ prints last 15 values in saturday for dictation """

    def check_input (self):
    """ Checks input of user """

    def right(self):
    """ Prints if all answers are right """
        print (" You got them all right !")
    
    def wrong(self):
    """ Prints that you had mistakes in dictation """
        print("You had {} mistakes")
    
    def try_again(self):
    """ Make a new try for the same dictatin """

    def where_mistake(self):
    """ prints where the mistakes are """


class morfix ():
    
    self.where_database = Vocabulary.add_to_database()
   
    def __init__ (self):
        pass

    def request(self):
    """ Return morfix file string """

    def morfix (self):
    """ takes values from responce """
        # Add stuff
        self.add_to_database(w,t)
    

v = Vocabulary("values.json")    

w, t = input("enter word:"), input("enter translation:") 






    


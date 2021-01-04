import json
import datetime
from bidi.algorithm import get_display 
from selenium import webdriver
import atexit



class Vocabulary():
    def __init__(self , json_path):
        self.__json_path = json_path
    def add_to_database(self,word, translation):
        with open(self.__json_path) as f:
            data = json.load(f)
        data[word] = translation
        with open(self.__json_path, 'w', encoding = 'utf8') as f:
            json.dump(data, f , indent = 4)

    def morfix (self):
        
        
        self.add_to_database(w,t)

v = Vocabulary("values.json")    

w, t = input("enter word:"), input("enter translation:") #need to add morfix values






    


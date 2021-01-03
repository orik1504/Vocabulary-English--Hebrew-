# -- imports --#
from datetime import datetime 
from selenium import webdriver
import atexit 
import json
from bidi.algorithm import get_display

# -- variables -- # 
path = 'C:/Users/ori/Desktop/programing/chromedriver/chromedriver.exe'
with open ('Vocabulary/values.json',encoding='utf8') as values:
    values = json.load(values)
print (values)
print(get_display("נייר")) # flips the word 

# -- enter values to json -- #

# -- prints current time -- #
now = datetime.now()
current_time = now.strftime("%H:%M")

# -- webdriver --#
wd = webdriver.Chrome(path)
atexit.register(lambda: wd.quit())
wd.get("https://www.morfix.co.il")

# -- vocabulary class --#
# class vocabulary:
#     def __init__(self):
#         pass
#     def check_words(self,webdriver,values,id): #takes random words from webdribver and dump them into json file
#         self.webdriver = webdriver
#         self.values = values
#         self.id = id
        
    
#     def dictation(self): #takes word from json file and asks for translation or spelling
        
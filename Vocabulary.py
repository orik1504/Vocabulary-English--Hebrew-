import json
import datetime
from bidi.algorithm import get_display 
from selenium import webdriver
import atexit



# -- function that dumps value to json file -- #
def write_in_json (translate , file ="Vocabulary/Vocabulary-English--Hebrew-/values.json"):
    with open ("Vocabulary/Vocabulary-English--Hebrew-/values.json", "w") as new_file:
        json.dump(translate,new_file)

# -- open the file and into the "words" list and append the value that I gave -- #
with open ("Vocabulary/Vocabulary-English--Hebrew-/values.json") as file:
    data = json.load(file) #what I already saved (dict "words" have value of list)
    in_data = data['words'] ##entering to "words" -  list of words in json fil
    value = {"paper":"1"} #need to make another value every time
    in_data.append(value) #append value to "words" list
    

print (in_data)

# # # # # # # # # #
# -- C H E C K -- #
# # # # # # # # # #

# -- get values to json file -- #
# vlaue = "orange"
# with open("Vocabulary/Vocabulary-English--Hebrew-/values.json",'w', encoding = 'utf8') as new_file: #open json file to write into as file
#   in_file = file['words']
#   in_file.append(vlaue)

# with open("Vocabulary/Vocabulary-English--Hebrew-/values.json") as file:
#     data = json.load(file) # dict "words" have value of list
#     in_data = data['words'] #entering to "words" -  list of words in json file 
# print (type(data))
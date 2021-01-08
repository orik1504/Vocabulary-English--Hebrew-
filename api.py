from bs4 import BeautifulSoup
import requests

class WordTranslationGenerator():
    
    URL = 'https://www.morfix.co.il/d/rand'
    TRANSLATION_CLASS = 'normal_translation_div'
    WORD_CLASS = 'Translation_spTop_heToen'

    def __request(self,):
        """ Return morfix file string """
        response = requests.get(self.URL)
        return BeautifulSoup(response.content,'lxml')

    def __word_from_soup (self, soup):
        return self.__text_by_element_class(soup, self.WORD_CLASS)

    def __translation_from_soup (self, soup):
        return self.__text_by_element_class(soup, self.TRANSLATION_CLASS)
    
    def __text_by_element_class(self, soup, class_name):
        
        element = soup.find(attrs={'class':class_name})

        if element is None:
            return None

        return element.getText().strip()

    def word_translation(self):
        soup = self.__request()
        word = self.__word_from_soup(soup)
        translation = self.__translation_from_soup(soup)

        if not all(item is not None for item in {word,translation}):
            return self.word_translation()
        
        return (word,translation)
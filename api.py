from bs4 import BeautifulSoup
import requests

class WordTranslationGenerator():
    
    URL = 'https://www.morfix.co.il/d/rand'
    TRANSLATION_CLASS = 'normal_translation_div'
    WORD_CLASS = 'Translation_spTop_heToen'

    @staticmethod
    def __request():
        """ Return morfix file string """
        response = requests.get(WordTranslationGenerator.URL)
        return BeautifulSoup(response.content,'lxml')

    @staticmethod
    def __word_from_soup (soup):
        return WordTranslationGenerator.__text_by_element_class(soup, WordTranslationGenerator.WORD_CLASS)
    
    @staticmethod
    def __translation_from_soup (soup):
        return WordTranslationGenerator.__text_by_element_class(soup, WordTranslationGenerator.TRANSLATION_CLASS)
    
    @staticmethod
    def __text_by_element_class(soup, class_name):
        
        element = soup.find(attrs={'class':class_name})

        if element is None:
            return None

        return element.getText().strip()

    @staticmethod
    def word_translation():
        soup = WordTranslationGenerator.__request()
        word = WordTranslationGenerator.__word_from_soup(soup)
        translation = WordTranslationGenerator.__translation_from_soup(soup)

        if not all(item is not None for item in {word,translation}):
            return WordTranslationGenerator.word_translation()
        
        return (word,translation)
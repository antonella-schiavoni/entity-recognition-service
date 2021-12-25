from typing import List

from src.entity_recognizers.entity_recognizer import EntityRecognizer
from src.entity_recognizers.utils import load_regex_list


class RegexEntityRecognizer(EntityRecognizer):
    """
    Entity recognizer object that applies regex to extract the information from the titles
    """

    def __init__(self):
        self.regex_list = load_regex_list()


    def extract_entities(self, title: List[str]):
        """
        Extract entities using the regexes loaded in self.regex_list
        """
        pass

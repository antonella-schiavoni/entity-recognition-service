import difflib
import logging
from typing import List
from src.entity import Entity, SpacyEntities
from src.entity_recognizers.entity_recognizer import EntityRecognizer
from src.entity_recognizers.utils import load_artists_list, load_synonyms


class SynonymEntityRecognizer(EntityRecognizer):
    """
    Entity recognizer object that matches against a synonym dictionary to extract the information from the event titles.
    """

    def __init__(self):
        self.synonyms = load_synonyms()
        self.artist_list = load_artists_list()

    def find_best_match(self, text: str) -> List[Entity]:
        """
        Find best match using difflib library
        """
        results = []
        entity_found = difflib.get_close_matches(text, self.artist_list)
        for entity_str in entity_found:
            if entity_str.lower() != text.lower():
                new_entity = Entity(
                    text=entity_str.title(), label=SpacyEntities.PERSON.name
                )
                results.append(new_entity)
                logging.info(
                    f"Entities found by SynonymEntityRecognizer: {new_entity.text}"
                )
        return results

    def extract_entities(self, title: List[str]) -> List[Entity]:
        """
        Look the title str in a synonym artists_list and return all artist associated
        """
        results = []
        for title_text in title:
            for artist_synonym in self.synonyms:
                if title_text in artist_synonym.get(
                    "value"
                ) or title_text in artist_synonym.get("synonyms"):
                    new_entity = Entity(text=title_text.title(), label="Artist")
                    results.append(new_entity)
                    logging.info(
                        f"Entities found by SynonymEntityRecognizer: {new_entity.text}"
                    )
            best_match = self.find_best_match(title_text)
            if best_match:
                results.extend(best_match)
        return results

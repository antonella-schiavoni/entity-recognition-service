import logging
from typing import List
from src.entity import Entity, SpacyEntities
from src.entity_recognizers.entity_recognizer import EntityRecognizer
from src.entity_recognizers.utils import load_artists_list


class ArtistEntityRecognizer(EntityRecognizer):
    """
    Entity recognizer object that looks for the artists names from a artists_list in the event titles.
    """

    def __init__(self):
        self.artists_list = load_artists_list()

    def extract_entities(self, title: List[str]) -> List[Entity]:
        """
        Entity recognizer object that iterates over the tokens of the title, and checks if that text is in the
        artists list. If it is, it creates an Entity objects and adds it to the list of results.
        """
        results = []
        for text in title:
            for artist in self.artists_list:
                if artist.lower() in text.lower():
                    new_entity = Entity(
                        text=artist.title(), label=SpacyEntities.PERSON.name
                    )
                    results.append(new_entity)
                    logging.info(
                        f"Entities found by ArtistEntityRecognizer: {new_entity.text}"
                    )
        return results

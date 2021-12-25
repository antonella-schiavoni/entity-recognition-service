import logging
import spacy
from typing import List
from src.entity import Entity
from src.entity_recognizers.entity_recognizer import EntityRecognizer


class SpacyEntityRecognizer(EntityRecognizer):
    """
    Entity recognizer object that applies spicy model to extract the information from the event titles.
    """

    def __init__(self):
        self.ner_model = spacy.load("en_core_web_lg")

    def extract_entities(self, title: List[str]) -> List[Entity]:
        """
        Given a processed event title, apply the Spacy Ner model to identify entities.
        For each entity found, create an Entity object with the event_title and the label.
        """
        results = []
        for text in title:
            ner_results = self.ner_model(text)
            for entity in ner_results.ents:
                new_entity = Entity(text=entity.text.title(), label=entity.label_)
                results.append(new_entity)
                logging.info(
                    f"Entities found by SpacyEntityRecognizer: {new_entity.text}"
                )
        return results

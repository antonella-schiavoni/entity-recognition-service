from src.entity import Entity, SpacyEntities
from src.entity_recognizers.entity_recognizer import EntityRecognizer
from src.processing import EventTitleProcessor
from typing import List, Dict


class EntityRecognizerManager:
    """
    Class that is in charge of calling the preprocess step and the entity recognizer algorithm.
    """

    def __init__(
            self,
            entity_recognizers: List[EntityRecognizer],
            event_title_processor: EventTitleProcessor,
    ):
        self.entity_recognizers = entity_recognizers
        self.event_title_processor = event_title_processor

    def build_results(self, entities_recognized: List[Entity]) -> Dict:
        """
        Given a list of entities, extract the text and several other entities, then  build a dictionary with the
        results. For the purpose of this challenge, I'm only returning the artists entities.
        """
        artists = []
        location = []
        date = []
        price = []
        for entity in entities_recognized:
            if entity.label == SpacyEntities.GPE.name:
                location.append(str(entity.text))
            elif entity.label == SpacyEntities.DATE.name:
                date.append(str(entity.text))
            elif entity.label == SpacyEntities.CARDINAL.name:
                price.append(str(entity.text))
            else:
                artists.append(str(entity.text))
        return {"artists": artists}

    def remove_duplicated_entities(self, entities: List[Entity]):
        """
        Remove duplicated Entity objects
        """
        return list(set(entities))

    def extract_entities(self, event_title: str) -> Dict[str, List[str]]:
        """
        Call the process method from the processor object and then extract the entities from that list of strings.
        After that, build the results object.
        """
        if event_title:
            title_processed = self.event_title_processor.process(event_title)
            entities = []
            for entity_recognizer in self.entity_recognizers:
                entities_recognized = entity_recognizer.extract_entities(title_processed)
                if entities_recognized:
                    entities.extend(entities_recognized)
            entities_dedupe = self.remove_duplicated_entities(entities)
            return self.build_results(entities_dedupe)
        else:
            return {"artists": []}

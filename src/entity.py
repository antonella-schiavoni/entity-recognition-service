from enum import Enum


class SpacyEntities(Enum):
    """
    Class to represent spacy entities as enum
    """

    PERSON = "PERSON"
    ORGANIZATION = "ORG"
    CARDINAL = "CARDINAL"
    DATE = "DATE"
    EVENT = "EVENT"
    GPE = "GPE"
    ORG = "ORG"
    PRODUCT = "PRODUCT"


def get_spacy_entity(entity: str) -> SpacyEntities:
    """
    Given a str, return thee spacy entity associated with it
    """
    if entity not in SpacyEntities.__members__:
        raise KeyError(f"Undefined entity {entity}")
    return SpacyEntities[entity]


class Entity:
    """
    Entity class is the object abstraction of spacy entities. It contains the text and the label identified.
    """

    def __init__(self, text: str, label: str):
        self.text = text
        self.label = label

    def __eq__(self, other):
        return self.text == other.text

    def __hash__(self):
        return hash(("text", self.text))


class EventTitle:
    """
    Event title abstraction that contains the event title and the list of entities identified.
    """

    def __init__(self, title):
        self.title = title
        self.entities = [Entity]

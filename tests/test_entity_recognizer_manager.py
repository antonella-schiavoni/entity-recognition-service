from _pytest.fixtures import fixture

from src.entity import Entity, SpacyEntities
from src.entity_recognizer_manager import EntityRecognizerManager
from src.entity_recognizers.artists_entity_recognizer import ArtistEntityRecognizer
from src.entity_recognizers.spacy_entity_recognizer import SpacyEntityRecognizer
from src.processing import EventTitleProcessor


@fixture
def entities():
    entity_1 = Entity(text="Roger Federer", label=SpacyEntities.PERSON.name)
    entity_2 = Entity(text="Lady Gaga", label=SpacyEntities.PERSON.name)
    return [entity_1, entity_2]


@fixture
def entities_duplicated():
    entity_1 = Entity(text="Roger Federer", label=SpacyEntities.PERSON.name)
    entity_2 = Entity(text="Roger Federer", label=SpacyEntities.PERSON.name)
    entity_3 = Entity(text="Lady Gaga", label=SpacyEntities.PERSON.name)
    entity_4 = Entity(text="Lady Gaga", label=SpacyEntities.PERSON.name)
    entity_5 = Entity(text="Lady Gaga", label=SpacyEntities.PERSON.name)
    return [entity_1, entity_2, entity_3, entity_4, entity_5]


@fixture
def entity_manager():
    processor = EventTitleProcessor()
    entity_recognizers = [ArtistEntityRecognizer(), SpacyEntityRecognizer()]
    return EntityRecognizerManager(
        event_title_processor=processor, entity_recognizers=entity_recognizers
    )


def test_build_results(entities, entity_manager):
    expected = {"artists": ["Roger Federer", "Lady Gaga"]}
    result = entity_manager.build_results(entities)
    assert result == expected


def test_remove_duplicated_entities(entities_duplicated, entity_manager):
    result = entity_manager.remove_duplicated_entities(entities_duplicated)
    assert len(result) == 2


def test_extract_entities(entity_manager):
    text = "Ed Sheeran at CenturyLink Field!"
    expected = "Ed Sheeran"
    result = entity_manager.extract_entities(event_title=text)
    assert expected in list(result.values())[0]

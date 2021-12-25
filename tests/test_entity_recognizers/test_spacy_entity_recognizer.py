from src.entity_recognizers.spacy_entity_recognizer import SpacyEntityRecognizer


def test_spacy_model_load():
    spacy_recognizer = SpacyEntityRecognizer()
    assert spacy_recognizer.ner_model


def test_spacy_extract_entities():
    spacy_recognizer = SpacyEntityRecognizer()
    title = "The Rolling Stones Story"
    result = spacy_recognizer.extract_entities([title])
    assert isinstance(result, list)
    assert result[0].text
    assert result[0].label

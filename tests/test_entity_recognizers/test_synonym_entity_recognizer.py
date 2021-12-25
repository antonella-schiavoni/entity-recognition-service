import pytest

from src.entity_recognizers.synonym_entity_recognizer import SynonymEntityRecognizer


@pytest.mark.parametrize(
    "title,expected",
    [("The Rolling Stones Story", "The Rolling Stones")],
)
def test_synonyms_extract_entities(title, expected):
    synonym_recognizer = SynonymEntityRecognizer()
    result = synonym_recognizer.extract_entities([title])
    assert isinstance(result, list)
    assert result[0].text == expected

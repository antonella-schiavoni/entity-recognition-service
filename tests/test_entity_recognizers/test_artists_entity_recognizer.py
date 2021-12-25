from src.entity_recognizers.artists_entity_recognizer import ArtistEntityRecognizer


def test_load_artist_list():
    artist_recognizer = ArtistEntityRecognizer()
    assert artist_recognizer.artists_list


def test_artist_extract_entities():
    artist_recognizer = ArtistEntityRecognizer()
    title = "The Rolling Stones Story"
    result = artist_recognizer.extract_entities([title])
    assert isinstance(result, list)
    assert result[0].text
    assert result[0].label

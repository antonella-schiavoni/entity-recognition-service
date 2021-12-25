from src.processing import EventTitleProcessor


def test_remove_characters():
    title = "This • is (just) a test"
    expected = "This  is just a test"
    processor = EventTitleProcessor()
    result = processor.remove_characters(title)
    assert result == expected


def test_split_text():
    title = "This & is - just, a test"
    expected = ["This", "is", "just", "a test"]
    processor = EventTitleProcessor()
    result = processor.split_text(title)
    assert result == expected


def test_process():
    title = (
        "Thursday •Sling Social, and Sling Library - with Kate Kirkby at Photography"
    )
    expected = [
        "Thursday Sling Social",
        "and Sling Library",
        "with Kate Kirkby at Photography",
    ]
    processor = EventTitleProcessor()
    result = processor.process(title)
    assert result == expected

import re
import logging
from typing import List


class EventTitleProcessor:
    """
    EventTitleProcessor responsibility is to apply rules to the event title with the intention of processing the
    event_title
    so it can be passed to an EntityRecognizer object.
    """

    CHARS_TO_REMOVE = ["•", "(", ")"]
    SPLIT_CHARS = "&|-|,"

    # TODO: evaluate in depth if I want to remove •
    def remove_characters(self, event_title: str) -> str:
        """
        Given an event title, remove special characters that do not add any value.

        Example:
        --------
        event_title: "Future • Russ Yallop • Bubba • 03-03-18"
        output: "Future  Russ Yallop  Bubba  03-03-18"
        """
        for char_to_remove in self.CHARS_TO_REMOVE:
            event_title = event_title.replace(char_to_remove, "")
        return event_title.strip()

    def split_text(self, event_title: str) -> List[str]:
        """
        Given an event title, split the text using a regex. The characters used for the split are defined in
        self.SPLIT_CHARS

        Example:
        --------
        event_title: "Alex the Astronaut & Stella Donnelly - Adelaide, SA"
        output: ['Alex the Astronaut', 'Stella Donnelly', 'Adelaide, SA']
        """
        result = re.split(self.SPLIT_CHARS, event_title)
        return [r.strip() for r in result]

    def process(self, event_title: str) -> List[str]:
        """
        Given an event title, remove noisy characters from it and afterwards split the text based on the characters
        defined in self.split_chars
        """
        text_processed = self.remove_characters(event_title)
        text_split = self.split_text(text_processed)
        logging.info(f"Text processed: {text_processed}")
        return text_split

import os
import json
from typing import List, Dict

ARTISTS_LIST_PATH = os.path.join(os.path.abspath("data/artists.txt"))
SYNONYM_PATH = os.path.join(os.path.abspath("data/synonyms.json"))


# REGEX_PATH = os.path.join(os.path.abspath("data/regex.json"))


def load_artists_list() -> List[str]:
    """
    This function loads the known artist from ARTISTS_LIST_PATH file and returns them in a list of strings.
    Ideally, this could be done using a db, but using a hardcoded approach for prototyping
    """
    result = []
    try:
        with open(ARTISTS_LIST_PATH) as file:
            lines = file.readlines()
            lines = [line.strip().lower() for line in lines]
            result.extend(lines)
    except OSError:
        print(f"Could not open/read file: {file}")
    return result


def load_synonyms() -> List[Dict]:
    """
    This function loads the synonyms from SYNONYM_PATH file and returns them in a list of dictionaries, containing
    one dictionary per synonym.
    Ideally, this could be done using a db, but using a hardcoded approach for prototyping
    """
    try:
        with open(SYNONYM_PATH, "r") as file:
            synonyms = json.load(file)
    except json.JSONDecodeError as exc:
        print(f"Could not open/read file: {file}. Exception: {exc}")
    return synonyms


def load_regex_list() -> List[str]:
    """
    This function loads the regexes defined in REGEX_PATH and returns them in a list.
    Ideally, this could be done using a db, but using a hardcoded approach for prototyping
    """
    pass

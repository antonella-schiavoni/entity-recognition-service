import logging
import time
from http.client import BAD_REQUEST

from flask import Flask, request, jsonify, abort
from src.entity_recognizer_manager import EntityRecognizerManager
from src.entity_recognizers.artists_entity_recognizer import ArtistEntityRecognizer
from src.entity_recognizers.spacy_entity_recognizer import SpacyEntityRecognizer
from src.entity_recognizers.synonym_entity_recognizer import SynonymEntityRecognizer
from src.processing import EventTitleProcessor
from src.schemas import EntitiesInputSchema

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
entities_input_schema = EntitiesInputSchema()


@app.route("/health", methods=["GET"])
def health():
    """Health endpoint"""
    return "ok"


@app.route("/entities", methods=["GET"])
def entities():
    """Compute entities from the given event_title"""
    start = time.time()

    # Request field validation
    errors = entities_input_schema.validate(dict(request.args))
    if errors:
        abort(BAD_REQUEST, str(errors))

    event_title = request.args.get("event_title")
    extracted_entities = manager.extract_entities(event_title=event_title)
    result = jsonify(extracted_entities)
    end = time.time()
    logging.info(f"Server request time: {end - start} seconds")
    return result


if __name__ == "__main__":
    processor = EventTitleProcessor()
    entity_recognizers = [
        ArtistEntityRecognizer(),
        SpacyEntityRecognizer(),
        SynonymEntityRecognizer(),
    ]
    manager = EntityRecognizerManager(
        entity_recognizers=entity_recognizers, event_title_processor=processor
    )
    app.run(host="0.0.0.0", port=5000)

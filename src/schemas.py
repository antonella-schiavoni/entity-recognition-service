from marshmallow import Schema, fields, validates, ValidationError
from marshmallow.validate import Length


class EntitiesInputSchema(Schema):
    """/entities - Get

    Parameters:
     - event_title (str)
    """
    event_title = fields.Str(
        required=True,
        validate=Length(max=10000),
        error_messages={"required": "The attribute event_title is required."},
        attribute="event_title",
    )

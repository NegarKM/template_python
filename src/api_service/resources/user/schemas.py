from marshmallow import Schema
from marshmallow.fields import String, Date


class UsersPOSTRequest(Schema):
    email = String(required=True)
    password = String(required=True)


class UserGETResponse(Schema):
    email = String()
    created_at = Date()

from marshmallow import Schema, fields


class MathFuncPowResultSchema(Schema):
    result = fields.Integer(required=True, description="", attribute="result")

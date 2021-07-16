from marshmallow import Schema, fields, validates_schema
from marshmallow.exceptions import ValidationError


class MathFuncPowRequestSchema(Schema):
    number = fields.Integer(allow_none=False, required=True)
    power = fields.Integer(allow_none=False, required=True)

    @validates_schema
    def validate_data(self, data, **kwargs):
        errors = {}
        if data['number'] <= 0:
            errors['number'] = "Number should be a positive number greater than 0"
        if data['power'] <= 0:
            errors['number'] = "Number should be a positive number greater than 0"

        if errors:
            raise ValidationError(errors)

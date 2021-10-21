from django.db import models


def validate_field(value):
    pass

class BiggerIntegerField(models.CharField):
    description = "Any integer that can't fit in BigIntegerField"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 150
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection) -> int:
        return int(value)

    def to_python(self, value):
        return int(value)

    

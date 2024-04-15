import json

from django.core.exceptions import ValidationError
from django.forms import fields, widgets


class ConstanceJSONField(fields.CharField):
    widget = widgets.Textarea

    def validate(self, value):
        try:
            json_value = json.loads(value)
        except:
            raise ValidationError("Invalid JSON")
        return super().validate(value)

    def clean(self, value):
        cleaned_value = super().clean(value)
        return json.dumps(json.loads(cleaned_value), indent=4)

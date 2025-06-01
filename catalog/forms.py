from django import forms
from django.db.models import BooleanField
from django.forms.widgets import DateTimeInput

from .models import MakeAnAppointment


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            elif isinstance(fild, forms.DateTimeField):
                fild.widget = DateTimeInput(
                    attrs={"type": "datetime-local", "class": "form-control"},
                )
            else:
                fild.widget.attrs["class"] = "form-control"


class MakeAnAppointmentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MakeAnAppointment
        fields = ["first_name", "middle_name", "last_name", "phone_number", "doctor", "date"]

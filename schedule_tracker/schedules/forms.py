from django import forms

from .models import Schedules


class ScheduleRegisterForm(forms.ModelForm):
    class Meta:
        model = Schedules
        fields = ["title", "date", "time", "memo", "task"]

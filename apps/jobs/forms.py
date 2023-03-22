from django import forms
from .models import Job


class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "title",
            "description",
            "qualifications",
            "min_salary",
            "max_salary",
            "application_details",
        ]

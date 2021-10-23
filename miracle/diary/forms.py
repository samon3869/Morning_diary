from django import forms
from .models import Diary

class DiaryForm(forms.ModelForm):

    class Meta:
        model = Diary
        exclude = ['dt_created', 'dt_modified']

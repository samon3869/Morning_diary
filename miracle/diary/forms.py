from django import forms
from .models import Diary, User

class DiaryForm(forms.ModelForm):

    class Meta:
        model = Diary
        exclude = ['dt_created', 'dt_modified']

class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["nickname"]

    def signup(self, request, user):
        user.nickname = self.cleaned_data["nickname"]
        user.save()
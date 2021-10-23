from django import forms

class DiaryForm(forms.Form):
    thanks = forms.CharField(label="감사", widget=forms.Textarea)
    feelgood = forms.CharField(label="기분좋게", widget=forms.Textarea)
    promise = forms.CharField(label="다짐", widget=forms.Textarea)
    donegood = forms.CharField(label="잘한일", widget=forms.Textarea)
    makegood = forms.CharField(label="좋게만든일", widget=forms.Textarea)

from django import forms


class MyForm(forms.Form):
    file = forms.FileField()

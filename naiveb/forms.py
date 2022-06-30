from django import forms

class UrlForm(forms.Form):
    url_link = forms.URLField()

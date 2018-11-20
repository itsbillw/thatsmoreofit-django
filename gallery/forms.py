from django import forms

class DocumentForm(forms.Form):
    docfile = forms.ImageField(
        label='Select a file',
    )

from django import forms 

class PositionForm(forms.Form):
    position = forms.CharField(label='Position', max_length=100)
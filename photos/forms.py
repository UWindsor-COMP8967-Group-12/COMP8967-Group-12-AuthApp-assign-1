from django import forms
from .models import Photo

class EditPhoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['category', 'description', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


    def __init__(self, *args, **kwargs):
        super(EditPhoto, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Select'
        self.fields['category'].required = False
        self.fields['description'].required = False
        self.fields['image'].required = False

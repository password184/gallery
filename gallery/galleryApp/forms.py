from django.forms import ModelForm
from django import forms
from .models import Gallery

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
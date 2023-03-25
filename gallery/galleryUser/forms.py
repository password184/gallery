from django.forms import ModelForm
from .models import About

class ProfileForm(ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
          super(ProfileForm, self).__init__(*args, **kwargs)

          for name, field in self.fields.items():
              field.widget.attrs['class'] = 'form-control'
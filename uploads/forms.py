from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.forms import ClearableFileInput, ModelForm, ValidationError, HiddenInput, IntegerField

from uploads.models import Photo, Category

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    # def __init__(self, *args, **kwargs):
    #     super(CustomUserCreationForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update(
    #         {'class': 'form-control', 'placeholder': 'Enter username...'})
    #     self.fields['password1'].widget.attrs.update(
    #         {'class': 'form-control', 'placeholder': 'Enter password...'})
    #     self.fields['password2'].widget.attrs.update(
    #         {'class': 'form-control', 'placeholder': 'Confirm password...'})




class PhotoForm(ModelForm):
    
    class Meta:
        model = Photo
        fields = '__all__'

class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User
from .models import *


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('Recipe_Title', 'Recipe_Ingredients', 'Recipe_Description',
                  'Recipe_Img','Recipe_Info','Recipe_Cat', 'Recipe_note')


class RegistraceForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class PrihlaseniForm(AuthenticationForm):
    class Meta:
        model = User

class AddCatForm(forms.ModelForm):
    class Meta:
        model = AddCat
        fields = ('Cat_Title', 'Cat_Description')

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('Recipe_Title', 'Recipe_Ingredients', 'Recipe_Description',
                  'Recipe_Info')


class RegistraceForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class PrihlaseniForm(AuthenticationForm):
    class Meta:
        model = User

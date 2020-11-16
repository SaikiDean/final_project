from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm, RegistraceForm, PrihlaseniForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def index(request):
    return render(request, '../templates/main.html', {})


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


def recipe_add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.Recipe_Author = request.user
            recipe.save()
            return redirect('recipe_details', recipe_title=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, '../templates/novy_recept.html', {'form': form})


def recipe_list(request):
    recipes = Recipe.objects.filter(Recipe_Date__lte=timezone.now()).order_by('Recipe_Date')
    return render(request, 'recipes/main.html', {'recipes': recipes})


def registrace(request):
    if request.method == "POST":
        form = RegistraceForm(request.POST)
        name = request.POST.get('username')
        passw = request.POST.get('password1')
        if form.is_valid():
            osoba = form.save()
            uziv = authenticate(username=name, password=passw)
            osoba.save()
            login(request, uziv)
            return redirect('/')
    else:
        form = RegistraceForm()
    return render(request, '../templates/register.html', {'form': form})


def prihlaseni(request):
    if request.method == 'POST':
        form = PrihlaseniForm(request, request.POST)
        name = request.POST.get('username')
        passw = request.POST.get('password')
        if form.is_valid:
            osoba = authenticate(username=name, password=passw)
            login(request, osoba)
            return redirect('/')
    else:
        form = PrihlaseniForm()
    return render(request, '../templates/login.html', {'form': form})

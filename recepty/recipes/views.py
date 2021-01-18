from django.shortcuts import render, redirect
from .models import Recipe, AddCat
from .forms import RecipeForm, RegistraceForm, PrihlaseniForm, AddCatForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def index(request):
    return render(request, '../templates/main.html', {})


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

def profile(request):
    return render(request, "../templates/profile.html")

def add_cat(request):
    if request.method == "POST":
        form = AddCatForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('/addcat', Cat_Title=category.pk)
    else:
        form = AddCatForm()
    return render(request, '../templates/addcat.html', {'form': form})


def recipe_add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.Recipe_Author = request.user
            recipe.save()
            return redirect('/details', recipe_title=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, '../templates/novy_recept.html', {'form': form})

def details(request, pk):
        recipe = Recipe.objects.get(pk=pk)
        return render(request, '../templates/details.html', {'recipe': recipe})

def cat_details(request):
    recipes = Recipe.objects.filter(Recipe_Date__lte=timezone.now()).order_by('Recipe_Date')
    return render(request, '../templates/cat_details.html', {'recipes': recipes})

def cat_list(request, pk):
    categories = AddCat.objects.get(pk=pk)
    return render(request, '../templates/catlist.html', {'categories': categories})

def recipe_list(request):
    recipes = Recipe.objects.filter(Recipe_Date__lte=timezone.now()).order_by('Recipe_Date')
    return render(request, '../templates/recipe_list.html', {'recipes': recipes})

def breakfast_list(request):
    recipes = Recipe.objects.filter(Recipe_Date__lte=timezone.now()).order_by('Recipe_Date')
    return render(request, '../templates/breakfast_snacks.html', {'recipes': recipes})

def lunch_list(request):
    recipes = Recipe.objects.filter(Recipe_Date__lte=timezone.now()).order_by('Recipe_Date')
    return render(request, '../templates/lunch_dinner.html', {'recipes': recipes})

def sweets_list(request):
    recipes = Recipe.objects.filter(Recipe_Date__lte=timezone.now()).order_by('Recipe_Date')
    return render(request, '../templates/healthy_sweets.html', {'recipes': recipes})

def drinks_list(request):
    recipes = Recipe.objects.filter(Recipe_Date__lte=timezone.now()).order_by('Recipe_Date')
    return render(request, '../templates/drinks.html', {'recipes': recipes})

def salad_list(request):
    recipes = Recipe.objects.filter(Recipe_Date__lte=timezone.now()).order_by('Recipe_Date')
    return render(request, '../templates/salad.html', {'recipes': recipes})

def soup_list(request):
    recipes = Recipe.objects.filter(Recipe_Date__lte=timezone.now()).order_by('Recipe_Date')
    return render(request, '../templates/soup.html', {'recipes': recipes})


def registrace(request):
    if request.method == "POST":
        form = RegistraceForm(request.POST)
        jmeno = request.POST.get('username')
        heslo = request.POST.get('password1')
        if form.is_valid():
            osoba = form.save()
            uzivatel = authenticate(username=jmeno, password=heslo)
            osoba.save()
            login(request, uzivatel)
            return redirect('/')
    else:
        form = RegistraceForm()
    return render(request, '../templates/register.html', {'form': form})


def prihlaseni(request):
    if request.method == 'POST':
        form = PrihlaseniForm(request, request.POST)
        jmeno = request.POST.get('username')
        heslo = request.POST.get('password')
        if form.is_valid:
            osoba = authenticate(username=jmeno, password=heslo)
            login(request, osoba)
            return redirect('/')
    else:
        form = PrihlaseniForm()
    return render(request, '../templates/login.html', {'form': form})


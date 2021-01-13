from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.prihlaseni, name="prihlaseni"),
    url(r'^register/$', views.registrace, name="registrace"),
    url(r'^logout/$', views.logout, name="logout"),
    path('novy/', views.recipe_add, name="recipe_add"),
    path('details/', views.recipe_list, name="recipe_list"),
    path('recipe/<int:pk>', views.details, name="details"),
    path('profile/', views.profile, name="profile"),
#odkazy na kategorie
    path('breakfast/', views.breakfast_list, name="breakfast_list"),
    path('drinks/', views.drinks_list, name="drinks_list"),
    path('sweets/', views.sweets_list, name="sweets_list"),
    path('lunch/', views.lunch_list, name="lunch_list"),
    path('salad/', views.salad_list, name="salad_list"),
    path('soup/', views.soup_list, name="soup_list"),
    ]

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.prihlaseni, name="prihlaseni"),
    url(r'^register/$', views.registrace, name="registrace"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^novy/$', views.recipe_add, name="recipe_add"),
]

from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('softicecream', views.softicecream, name='softicecream'),
    path('deal', views.deal, name='deal'),
    path('familypack', views.familypack, name='familypack'),


]

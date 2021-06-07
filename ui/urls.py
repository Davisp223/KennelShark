from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.ui, name='ui')

]

from django.urls import path, include
from . import views

app_name = 'Movie'

urlpatterns = [

    path('', views.index, name='index'),
]

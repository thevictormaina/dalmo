from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('moments', views.all_moments, name="all_moments"),
    path('entries', views.all_entries, name="all_entries"),
]
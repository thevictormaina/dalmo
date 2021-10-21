from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    ctx = { 
        "title": "Know Yourself",
        "daily_rating": 3, # Change to entry object
        "tidiness_rating": 2, # Change as well
        }
    return render(request, 'main/index.html', ctx)
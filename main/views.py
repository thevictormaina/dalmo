from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    ctx = { "title": "Know Yourself" }
    return render(request, 'main/index.html', ctx)
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

today = timezone.now()
week_ago = today - timezone.timedelta(days=7)

def index(request):
    if request.GET:
        from_date = request.GET['from-date']
        to_date = request.GET['to-date']
        print(True)
    else:
        from_date = week_ago.strftime('%Y-%m-%d')
        to_date = today.strftime('%Y-%m-%d')
        print(from_date)

    ctx = { 
        "title": "Know Yourself",
        "from_date": from_date,
        "to_date": to_date,
        "daily_rating": 3, # Change to entry object
        "tidiness_rating": 2, # Change as well
        }
    return render(request, 'main/index.html', ctx)

def all_moments(request):
    ctx = {}
    return render(request, 'main/all_moments.html', ctx)
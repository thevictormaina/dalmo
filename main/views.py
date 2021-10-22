from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from main.models import Moment

today = timezone.now()
week_ago = today - timezone.timedelta(days=7)

def index(request):
    if request.GET:
        from_date = request.GET['from-date']
        to_date = request.GET['to-date']
    else:
        from_date = week_ago.strftime('%Y-%m-%d')
        to_date = today.strftime('%Y-%m-%d')

    moments = Moment.date_range(from_date, to_date)
    emotions = Moment.count_emotions(from_date, to_date)
    emotions.sort(key=lambda f: f['count'], reverse=True)

    ctx = { 
        "title": "Know Yourself",
        "from_date": from_date,
        "to_date": to_date,
        "moments_number": len(moments),
        "emotions": emotions,
        "daily_rating": 3, # Change to entry object
        "tidiness_rating": 2, # Change as well
        }

    return render(request, 'main/index.html', ctx)

def all_moments(request):
    if request.GET:
        from_date = request.GET['from-date']
        to_date = request.GET['to-date']
    else:
        from_date = week_ago.strftime('%Y-%m-%d')
        to_date = today.strftime('%Y-%m-%d')

    ctx = { 
        "title": "Entries",
        "from_date": from_date,
        "to_date": to_date,
        }
    return render(request, 'main/all_moments.html', ctx)
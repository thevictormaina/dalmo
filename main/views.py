from datetime import tzinfo
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from main.models import Entry, Moment

today = timezone.localtime()
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
    entries = Entry.date_range(from_date, to_date)
    check_entry = True if len(entries) > 0 else False
    average_rating = Entry.average_rating(from_date, to_date)
    sleep_duration = Entry.average_sleep_duration(from_date, to_date)
    average_meals = Entry.average_meals_amount(from_date, to_date)
    average_water = Entry.average_water_amount(from_date, to_date)
    average_tidiness = Entry.average_tidiness_rating(from_date, to_date)

    ctx = { 
        "title": "Know Yourself",
        "from_date": from_date,
        "to_date": to_date,
        "moments_number": len(moments),
        "emotions": emotions,
        "check_entry": check_entry,
        "entries_amount": len(entries),
        "average_rating": average_rating,
        "sleep_duration": sleep_duration,
        "average_meals": average_meals,
        "average_water": average_water,
        "average_tidiness": average_tidiness
        }

    return render(request, 'main/index.html', ctx)

def all_moments(request):
    if request.GET:
        from_date = request.GET['from-date']
        to_date = request.GET['to-date']
    else:
        from_date = week_ago.strftime('%Y-%m-%d')
        to_date = today.strftime('%Y-%m-%d')

    moments_by_date = Moment.sort_by_date(from_date, to_date)
    
    print("DATES: ", moments_by_date, "\n")
    print(to_date)


    ctx = { 
        "title": "Entries",
        "from_date": from_date,
        "to_date": to_date,
        "moments_by_date": moments_by_date
        }
    return render(request, 'main/all_moments.html', ctx)

def all_entries(request):
    ctx = {}
    return render(request, "main/all_entries.html", ctx)
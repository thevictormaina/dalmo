from datetime import tzinfo
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from main.models import Entry, Moment

today = timezone.localtime()
week_ago = today - timezone.timedelta(days=7)

def index(request):
    from_date = None
    to_date = None

    if request.GET:
        from_date = request.GET['from-date'] if len(request.GET['from-date']) > 0 else None
        to_date = request.GET['to-date'] if len(request.GET['to-date']) > 0 else None

    print(f"FROM_DATE 1: {from_date}")

    moments = Moment.list_moments(from_date=from_date, to_date=to_date)
    entries = Entry.list_entries(from_date=from_date, to_date=to_date)
    ctx = { 
        "title": "Know Yourself",
        "from_date": from_date,
        "to_date": to_date,
        "moments_number": len(moments),
        "emotions": Moment.count_emotions(from_date=from_date, to_date=to_date),
        "check_entry": Entry.list_entries(from_date=from_date, to_date=to_date),
        "entries_amount": len(entries),
        "average_rating": Entry.average_rating(from_date=from_date, to_date=to_date),
        "sleep_duration": Entry.average_sleep_duration(from_date=from_date, to_date=to_date),
        "average_meals": Entry.average_meals_amount(from_date=from_date, to_date=to_date),
        "average_water": Entry.average_water_amount(from_date=from_date, to_date=to_date),
        "average_tidiness": Entry.average_tidiness_rating(from_date=from_date, to_date=to_date)
        }

    return render(request, 'main/index.html', ctx)

def all_moments(request):
    if request.GET:
        from_date = request.GET['from-date'] if len(request.GET['from-date']) > 0 else None
        to_date = request.GET['to-date'] if len(request.GET['to-date']) > 0 else None
        search_term = request.GET['search']
    else:
        from_date = None
        to_date = None
        search_term = ""

    moments_by_date = Moment.by_date(from_date, to_date, search_term)

    ctx = { 
        "title": "Entries",
        "from_date": from_date,
        "to_date": to_date,
        "moments_by_date": moments_by_date,
        "search_term": search_term
        }
    return render(request, 'main/all_moments.html', ctx)

def all_entries(request):
    ctx = {}
    return render(request, "main/all_entries.html", ctx)
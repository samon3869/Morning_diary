import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Diary

def index(request):
    return render(request, 'diary/index.html')

def today_dairy(request, username):
    today = datetime.datetime.now()
    today_humandate = today.strftime("%Y-%m-%d")
    today_diary = Diary.objects.filter(dt_created__date=today_humandate)
    if today_diary:
        context = {
            "username": username,
            "today_diary": today_diary[0],
            "thanks_list": today_diary[0].thanks.split(", "),
            "feelgood_list": today_diary[0].feelgood.split(", "),
            "promise_list": today_diary[0].promise.split(", "),
            "donegood_list": today_diary[0].donegood.split(", "),
            "makegood_list": today_diary[0].makegood.split(", ")
        }
    else:
        context = {
            "username": username,
        }

    return render(request, 'diary/today_diary.html', context=context)
# Create your views here.

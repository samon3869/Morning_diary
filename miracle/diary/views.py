import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Diary

def index(request):
    return render(request, 'diary/index.html')

def today_dairy(request, username):
    today = datetime.datetime.now()
    today_humandate = today.strftime("%Y-%m-%d")
    today_diary = Diary.objects.get(dt_created__date=today_humandate)
    context = {
        "username": username,
        "today_diary": today_diary,
        "thanks_list": today_diary.thanks.split(", "),
        "feelgood_list": today_diary.feelgood.split(", "),
        "promise_list": today_diary.promise.split(", "),
        "donegood_list": today_diary.donegood.split(", "),
        "makegood_list": today_diary.makegood.split(", ")
    }

    return render(request, 'diary/today_diary.html', context=context)
# Create your views here.

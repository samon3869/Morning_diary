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
    print(today_diary)
    context = {
        "username":username,
        "today_diary":today_diary
    }
    return render(request, 'diary/today_diary.html', context=context)
# Create your views here.

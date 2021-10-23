import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Diary
from .forms import DiaryForm

def index(request):
    return render(request, 'diary/index.html')

def today_diary_create(request):
    if request.method == 'POST':
        thanks = request.POST['thanks']
        feelgood = request.POST['feelgood']
        promise = request.POST['promise']
        donegood = request.POST['donegood']
        makegood = request.POST['makegood']
        new_diary = Diary(
            thanks = thanks,
            feelgood = feelgood,
            promise = promise,
            donegood = donegood,
            makegood =makegood,
        )
        new_diary.save()
        return redirect('today-diary', username='keon')
    else:
        diary_form = DiaryForm()
        return render(request, 'diary/diary_form.html', {'form': diary_form})

def today_dairy(request, username):
    today = datetime.datetime.now()
    today_humandate = today.strftime("%Y-%m-%d")
    today_diary = Diary.objects.filter(dt_created__date=today_humandate).order_by('-dt_created',)
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

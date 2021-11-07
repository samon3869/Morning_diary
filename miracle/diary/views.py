import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from allauth.account.views import PasswordChangeView
from .models import Diary
from .forms import DiaryForm

def index(request):
    return render(request, 'diary/index.html')

def today_diary_create(request):
    if request.method == 'POST':
        diary_form = DiaryForm(request.POST)
        diary_form.instance.author = request.user
        diary_form.save()
        return redirect('today-diary', username=request.user.username)
    else:
        diary_form = DiaryForm()
        return render(request, 'diary/diary_form.html', {'form': diary_form})

def today_dairy(request, username):
    today = datetime.datetime.now()
    today_humandate = today.strftime("%Y-%m-%d")
    today_diary = Diary.objects.filter(author = request.user).filter(dt_created__date=today_humandate).order_by('-dt_created',)
    if today_diary:
        today_diary=today_diary[0]
        context = {
            "username": username,
            "today_diary": today_diary,
            "thanks_list": today_diary.thanks.split(", "),
            "feelgood_list": today_diary.feelgood.split(", "),
            "promise_list": today_diary.promise.split(", "),
            "donegood_list": today_diary.donegood.split(", "),
            "makegood_list": today_diary.makegood.split(", ")
        }
    else:
        context = {
            "username": username,
        }

    return render(request, 'diary/today_diary.html', context=context)


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')

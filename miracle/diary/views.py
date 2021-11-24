import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from allauth.account.views import PasswordChangeView
from .models import Diary, FriendsApply, User
from .forms import DiaryForm

def index(request):
    return render(request, 'diary/index.html')

# [datetime global varibles]

today = datetime.datetime.now()
today_humandate = today.strftime("%Y-%m-%d")

# [diary create or update view] if today_diary already exists, update diary

def today_diary_create(request):
    if request.method == 'POST':
        diary_form = DiaryForm(request.POST)
        diary_form.instance.author = request.user
        diary_form.save()
        return redirect('today-diary', username=request.user.username)
    else:
        diary_form = DiaryForm()
        return render(request, 'diary/diary_form.html', {'form': diary_form})

def today_diary_update(request, diary_id):
    today_diary_gotten = Diary.objects.get(id=diary_id)
    if request.method == 'POST':
        diary_form = DiaryForm(request.POST, instance=today_diary_gotten)
        if diary_form.is_valid():
            diary_form.save()
            return redirect('today-diary', username=request.user.username)
    else:
        diary_form = DiaryForm(instance=today_diary_gotten)
        return render(request, 'diary/diary_form.html', {'form': diary_form})

def today_diary_write(request):
    today_diary = Diary.objects.filter(author = request.user).filter(dt_created__date=today_humandate)
    if today_diary:
        diary_id = today_diary[0].id
        return today_diary_update(request, diary_id)
    else:
        return today_diary_create(request)

# [diarylist view]

def today_dairy(request, username):
    today_diary = Diary.objects.filter(author = request.user).filter(dt_created__date=today_humandate)
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


# [frends view]

def friends(request, username):
    friend_list = User.objects.get(username = username).friends.all()
    context = {
        "friend_list": friend_list
    }
    return render(request, 'friends/friends.html', context=context)

def add_friends(request, username):
    applying_list = FriendsApply.objects.filter(user_from=username).filter(ok_sign=0)
    be_applied_list = FriendsApply.objects.filter(user_to=request.user.pk).filter(ok_sign=0)
    context = {
        "applying_list": applying_list,
        "be_applied_list": be_applied_list
    }
    return render(request, 'friends/add_friends.html', context=context)

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')

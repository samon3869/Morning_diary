from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'diary/index.html')

def today_dairy(request, username):
    context = {
        "username":username
    }
    return render(request, 'diary/today_diary.html', context=context)
# Create your views here.

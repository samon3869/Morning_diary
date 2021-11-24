from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('today_diary/new/', views.today_diary_write, name='diary-create'),
    path('today_diary/<str:username>/', views.today_dairy, name='today-diary'),
    path('friends/<str:username>/', views.friends, name='friends'),
]

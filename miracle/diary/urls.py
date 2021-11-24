from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('today_diary/new/', views.today_diary_write, name='diary-create'),
    path('today_diary/<str:username>/', views.today_dairy, name='today-diary'),
    path('friends/<str:username>/', views.friends, name='friends'),
    path('friends/<str:username>/add_friends/', views.add_friends, name='add-friends'),
    path('friends/<str:username>/apply_friends/', views.apply_friends, name='apply-friends'),
]

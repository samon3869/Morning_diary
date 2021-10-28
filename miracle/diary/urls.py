from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('today_diary/new/', views.today_diary_create, name='diary-create'),
    path('today_diary/<str:username>/', views.today_dairy, name='today-diary'),
]

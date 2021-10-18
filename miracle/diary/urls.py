from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index),
    path('today_diary/', views.today_dairy),
]

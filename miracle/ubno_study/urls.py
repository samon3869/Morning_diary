from django.urls import path
from . import views

urlpatterns = [
	path('', views.MyStudyTime.as_view(), name='my-study-time'),
]
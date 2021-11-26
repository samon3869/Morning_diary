from django.urls import path
from . import views

urlpatterns = [
	path('<int:user_id>/', views.MyStudyTime.as_view(), name='my-study-time'),
]
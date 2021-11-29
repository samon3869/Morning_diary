from django.urls import path
from .views import handover_data_views

urlpatterns = [
	path('<int:user_id>/', handover_data_views.MyStudyTime.as_view(), name='my-study-time'),
]
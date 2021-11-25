from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('today_diary/new/', views.today_diary_write, name='diary-write'),
    path('today_diary/new/create/', views.TodayDiaryCreate.as_view(), name='diary-create'),
    path('today_diary/new/update/<int:diary_id>/', views.TodayDiaryUpdate.as_view(), name='diary-update'),
    path('today_diary/<int:user_id>/', views.TodayDiary.as_view(), name='today-diary'),
    path('today_diary/see_diary/<int:diary_id>/', views.SeeDiary.as_view(), name='see-diary'),
    path('today_diary/<int:pk>/friends_diary/', views.FriendsDiary.as_view(), name='friends-diary'),
    path('friends/<str:username>/', views.friends, name='friends'),
    path('friends/<str:username>/add_friends/', views.add_friends, name='add-friends'),
    path('friends/<str:username>/apply_friends/', views.apply_friends, name='apply-friends'),
]

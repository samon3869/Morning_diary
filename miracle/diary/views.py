import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.views import PasswordChangeView
from .models import Diary, FriendsApply, User
from .forms import DiaryForm

def index(request):
    return render(request, 'diary/index.html')

# [datetime global varibles]

today = datetime.datetime.now()
today_humandate = today.strftime("%Y-%m-%d")

# [diary create or update view] if today_diary already exists, update diary

# def today_diary_create(request):
#     if request.method == 'POST':
#         diary_form = DiaryForm(request.POST)
#         diary_form.instance.author = request.user
#         diary_form.save()
#         return redirect('today-diary', username=request.user.username)
#     else:
#         diary_form = DiaryForm()
#         return render(request, 'diary/diary_form.html', {'form': diary_form})
class TodayDiaryCreate(LoginRequiredMixin, CreateView):
    model = Diary
    form_class = DiaryForm
    template_name = 'diary/diary_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('today-diary', kwargs={'user_id': self.object.author.pk})


# def today_diary_update(request, diary_id):
#     today_diary_gotten = Diary.objects.get(id=diary_id)
#     if request.method == 'POST':
#         diary_form = DiaryForm(request.POST, instance=today_diary_gotten)
#         if diary_form.is_valid():
#             diary_form.save()
#             return redirect('today-diary', username=request.user.username)
#     else:
#         diary_form = DiaryForm(instance=today_diary_gotten)
#         return render(request, 'diary/diary_form.html', {'form': diary_form})
class TodayDiaryUpdate(LoginRequiredMixin, UpdateView):
    model = Diary
    form_class = DiaryForm
    template_name = 'diary/diary_form.html'
    pk_url_kwarg = 'diary_id'
    
    def get_success_url(self):
        return reverse('today-diary', kwargs={'user_id': self.object.author.pk})


def today_diary_write(request):
    today_diary = Diary.objects.filter(author = request.user).filter(dt_created__date=today_humandate)
    if today_diary:
        diary_id = today_diary[0].id
        return redirect('diary-update', diary_id)
    else:
        return redirect('diary-create')

# [diarylist view]

# def today_dairy(request, user_id):
#     today_diary = Diary.objects.filter(author = request.user).filter(dt_created__date=today_humandate)
#     if today_diary:
#         today_diary=today_diary[0]
#         context = {
#             "user_id": user_id,
#             "today_diary": today_diary,
#             "thanks_list": today_diary.thanks.split(", "),
#             "feelgood_list": today_diary.feelgood.split(", "),
#             "promise_list": today_diary.promise.split(", "),
#             "donegood_list": today_diary.donegood.split(", "),
#             "makegood_list": today_diary.makegood.split(", ")
#         }
#     else:
#         context = {
#             "user_id": user_id,
#         }

#     return render(request, 'diary/today_diary.html', context=context)
class TodayDiary(LoginRequiredMixin, UserPassesTestMixin, View):
    raise_exception = True
    
    def get(self, request, user_id):
        today_diary = Diary.objects.filter(author = request.user).filter(dt_created__date=today_humandate)
        if today_diary:
            today_diary=today_diary[0]
            context = {
                "user_id": user_id,
                "diary": today_diary,
                "thanks_list": today_diary.thanks.split(", "),
                "feelgood_list": today_diary.feelgood.split(", "),
                "promise_list": today_diary.promise.split(", "),
                "donegood_list": today_diary.donegood.split(", "),
                "makegood_list": today_diary.makegood.split(", ")
            }
        else:
            context = {
                "user_id": user_id,
            }
            
        return render(request, 'diary/today_diary.html', context=context)

    def test_func(self, user):
        target_user_id = self.kwargs['user_id']
        # 타겟유저본인이거나
        be_me = (target_user_id == user.pk)
        # 타겟유저의친구거나
        target_friends = list(User.objects.get(pk=target_user_id).friends.all())
        be_freind = (user in target_friends)
        
        return be_me or be_freind
    
    
# [see diary]
class SeeDiary(LoginRequiredMixin, UserPassesTestMixin, View):
    raise_exception = True
    
    def get(self, request, diary_id):
        target_diary = Diary.objects.get(pk=diary_id)
        context = {
            "diary": target_diary,
            "user": target_diary.author,
            "user_id": target_diary.author.pk,
            "target_diary": target_diary,
            "thanks_list": target_diary.thanks.split(", "),
            "feelgood_list": target_diary.feelgood.split(", "),
            "promise_list": target_diary.promise.split(", "),
            "donegood_list": target_diary.donegood.split(", "),
            "makegood_list": target_diary.makegood.split(", ")
        }

            
        return render(request, 'diary/today_diary.html', context=context)

    def test_func(self, user):
        diary_id = self.kwargs['diary_id']
        # 타겟유저본인이거나
        target_user_id = Diary.objects.get(pk=diary_id).author.pk
        be_me = (target_user_id == user.pk)
        # 타겟유저의친구거나
        target_friends = list(User.objects.get(pk=target_user_id).friends.all())
        be_freind = (user in target_friends)
        
        return be_me or be_freind



# [friends diarylist]

class FriendsDiary(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'diary/friends_diary.html'
    pk_url_kwarg = "pk"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_pk = self.kwargs.get("pk")
        friend_list = User.objects.get(pk=user_pk).friends.all()
        # 친구 리스트로부터 친구 글 링크랑, 친구 글 내용 일부 받아오기
        friend_diary_list = []
        for friend in friend_list:
            today_diary = Diary.objects.filter(author=friend.pk).order_by('-dt_modified')
            if today_diary:
                today_diary=today_diary[0]
                diary_data = {
                    "diary_id": today_diary.pk,
                    "username": friend.username,
                    "today_diary": today_diary,
                    "thanks": today_diary.thanks.split(", ")[0],
                    "donegood": today_diary.donegood.split(", ")[0],
                    "dt_modified": today_diary.dt_modified
                }
                friend_diary_list.append(diary_data)
            else:
                diary_data = {
                    "username": friend.username,
                    "dt_modified": 0
                }
                friend_diary_list.append(diary_data)
            friend_diary_list.sort(key=lambda x:x["dt_modified"], reverse=True)
        context["friend_diary_list"] = friend_diary_list
        return context


# [frends view]

def friends(request, username):
    friend_list = User.objects.get(username = username).friends.all()
    context = {
        "friend_list": friend_list
    }
    return render(request, 'friends/friends.html', context=context)

def add_friends(request, username):
    if request.method == 'POST':
        confirm = request.POST['ok']
        pk = request.POST['list_pk']
        target = FriendsApply.objects.get(pk=pk)
        if confirm == "positive":
            friend = User.objects.get(username=target.user_from)
            me = request.user
            friend.friends.add(me)
            me.friends.add(friend)
            friend.save()
            me.save()
            target.delete()
        elif confirm == "negative":
            target.delete()
        return redirect('add-friends', username=request.user.username)
    else:
        applying_list = FriendsApply.objects.filter(user_from=username).filter(ok_sign=0)
        be_applied_list = FriendsApply.objects.filter(user_to=request.user.pk).filter(ok_sign=0)
        context = {
            "applying_list": applying_list,
            "be_applied_list": be_applied_list
        }
        return render(request, 'friends/add_friends.html', context=context)
    
def apply_friends(request, username):
    if request.method == 'POST':
        friend_name = request.POST['name']
        try:
            friend = User.objects.get(username=friend_name)
            FriendsApply.objects.create(
                user_from=username,
                user_to=friend,
            )
        except:
            pass
    return redirect('add-friends', username=request.user.username)

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')

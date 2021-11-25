from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import constraints
from .validators import validate_no_special_characters

# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(
        max_length=15, 
        unique=True, 
        null=True,
        validators=[validate_no_special_characters],
        error_messages={'unique': '이미 사용중인 닉네임입니다.'},
    )
    friends = models.ManyToManyField('self', blank=True)
    
    def __str__(self):
        return self.email


class Diary(models.Model):
    # 감사일기3, 잘한일기3, 마지막 수정일
    thanks = models.TextField(blank=True, null=True)
    feelgood = models.TextField(blank=True, null=True)
    promise = models.TextField(blank=True, null=True)
    donegood = models.TextField(blank=True, null=True)
    makegood = models.TextField(blank=True, null=True)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        human_date = self.dt_created.strftime("%Y-%m-%d")
        return human_date
    

class FriendsApply(models.Model):
    user_from = models.CharField(max_length=199)
    user_to = models.ForeignKey(User, on_delete=models.CASCADE)
    ok_sign = models.BooleanField(default=False)
    
    class Meta:
        
        constraints = [
            models.UniqueConstraint(
                fields=["user_from", "user_to"],
                name="unique apply",
            ),
        ]
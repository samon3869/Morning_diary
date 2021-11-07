from django.db import models
from django.contrib.auth.models import AbstractUser
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
    
    def __str__(self):
        return self.email


class Diary(models.Model):
    # 감사일기3, 잘한일기3, 마지막 수정일
    thanks = models.TextField()
    feelgood = models.TextField()
    promise = models.TextField()
    donegood = models.TextField()
    makegood = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        human_date = self.dt_created.strftime("%Y-%m-%d")
        return human_date

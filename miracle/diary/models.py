from django.db import models

# Create your models here.

class Diary(models.Model):
    # 감사일기3, 잘한일기3, 마지막 수정일
    thanks = models.TextField()
    feelgood = models.TextField()
    promise = models.TextField()
    donegood = models.TextField()
    makegood = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        human_date = self.dt_created.strftime("%Y-%m-%d")
        return human_date
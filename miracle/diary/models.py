from django.db import models

# Create your models here.

class Diary(models.Model):
    # 감사일기3, 잘한일기3, 마지막 수정일
    thanks_1 = models.TextField()
    thanks_2 = models.TextField()
    thanks_3 = models.TextField()
    done_good_1 = models.TextField()
    done_good_2 = models.TextField()
    done_good_3 = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        human_date = self.dt_created.strftime("%Y-%m-%d")
        return human_date
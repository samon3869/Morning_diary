from django.shortcuts import render
from django.views import View

# Create your views here.
class MyStudyTime(View):
    def get(self, request):
        return render(request, 'ubno_study/my_study_time.html')
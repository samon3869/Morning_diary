import pandas as pd
import os
from django.shortcuts import render
from django.views import View

# Create your views here.
class MyStudyTime(View):
    def get(self, request, user_id):
        module_dir = os.path.dirname(__file__) 
        file_path = os.path.join(module_dir, 'static', 'ubno_study', 'dummydata', 'study_time_table.csv')
        df = pd.read_csv(file_path)
        df_for_html = df.to_html()
        context = {
            'df': df_for_html,
        }
        return render(request, 'ubno_study/my_study_time.html', context=context)
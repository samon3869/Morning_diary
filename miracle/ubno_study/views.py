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
        # labels, data 넘겨주기
        labels = list(df['dt_created'])
        author = df['author'].unique()
        datasets = [{
            # labels: 사람
            "author": author[0],
            # data: 공부시간데이터
            "data": list(df.loc[df['author'] == author[0], 'minutes'])
        }]
        context = {
            "labels": labels,
            "datasets": datasets
        }
        return render(request, 'ubno_study/my_study_time.html', context=context)
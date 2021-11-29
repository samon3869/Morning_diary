import pandas as pd
import os
import json
from django.shortcuts import render
from django.views import View
from . import date_calculator
import datetime

# Create your views here.
class MyStudyTime(View):
    def get(self, request, user_id):
        day = request.GET.get('day')
        day = datetime.datetime.strptime(day, "%m/%d/%Y")
        week_days = date_calculator.get_week_days(day)
        module_dir = os.path.dirname(__file__) 
        file_path = os.path.join(module_dir, '..', 'static', 'ubno_study', 'dummydata', 'study_time_table.csv')
        df = pd.read_csv(file_path)
        
        # 그래프 그리기용 테이블로 정리하기       
        author = df['author'].unique()
        table_for_graph = pd.DataFrame({'dt_created': week_days})
        for i in range(len(author)):
            dataset = df.loc[df['author'] == author[i], ['dt_created', 'minutes']]
            dataset.rename(columns = {'minutes': author[i]}, inplace = True)
            table_for_graph = pd.merge(table_for_graph, dataset, on='dt_created', how='left')
            
        # 1. labels
        labels = list(table_for_graph['dt_created'])
        # color set
        colors = ['#FF7F50', '#DE3163', '#9FE2BF',  '#FFBF00','#40E0D0', '#6495ED', '#DFFF00', '#CCCCFF']
        # 2. datasets
        datasets = []
        column_length = table_for_graph.shape[1] - 1
        for i in range(column_length):
            series = table_for_graph.iloc[:, i+1]
            dataset = {
                "label": series.name,
                "data": list(series),
                "backgroundColor": colors[i],
                "Color": colors[i],
                "borderColor": colors[i]
            }
            datasets.append(dataset)
        datasets = json.dumps(datasets)
        today = datetime.datetime.today().strftime("%m/%d/%Y")
        # context로 넘겨주기
        context = {
            "labels": labels,
            "datasets": datasets,
            "today": today
        }
        return render(request, 'ubno_study/my_study_time.html', context=context)

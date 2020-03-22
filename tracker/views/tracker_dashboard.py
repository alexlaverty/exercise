from .. import forms
from ..models import Entries
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.http import HttpResponse
from django.shortcuts import render
import logging
import pandas as pd
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

@login_required(login_url="/users/login/")
def tracker_dashboard(request):

    ## EXERCISE

    exercise_entry_queryset = Entries.objects.filter(Username=request.user,Tracking="Exercise")\
                                             .exclude(Additional_Information="Skipped")\
                                             .values('Date','String_Value')
    exercise_labels = []
    exercise_data = []
    
    if exercise_entry_queryset:
        df_exercise = pd.DataFrame(list(exercise_entry_queryset))
        today = (pd.Timestamp("today") - pd.DateOffset(days=13)).strftime("%m-%d-%Y")
        idx = pd.Series(pd.date_range(today,periods=14))
        df_exercise.index = df_exercise['Date']
        del df_exercise['Date']

        df_exercise = df_exercise.groupby(df_exercise.index)\
               .count()\

        df_exercise = df_exercise.reindex(idx, fill_value=0)

        exercise_labels = df_exercise.index.tolist()
        exercise_labels = [ exercise_label.strftime("%d %b") for exercise_label in exercise_labels]
        exercise_data = df_exercise["String_Value"].tolist()


    return render(request, 'tracker/tracker_dashboard.html',
                    {
                        'exercise_labels' : exercise_labels,
                        'exercise_data' : exercise_data
                    } )

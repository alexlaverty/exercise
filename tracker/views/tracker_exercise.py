from .. import forms
from ..models import Entries
from ..models import Exercise
from ..models import UserProfile
from ..tables import EntriesTable
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
import logging

logging.basicConfig(level=logging.DEBUG)

def tracker_exercise(request):
    if request.method == 'POST':
        #post_exercise_id = request.GET['exercise_id']
        if request.POST.get('skip_exercise_id'):
            skip_exercise_id = request.POST['skip_exercise_id']
            logging.debug('POST - Skip Exercise : {}'.format(skip_exercise_id))
            Entries.objects.filter(id=skip_exercise_id).update(Additional_Information="Skipped")
        if request.POST.get('complete_exercise_id'):
            complete_exercise_id = request.POST['complete_exercise_id']
            logging.debug('POST - Complete Exercise : {}'.format(complete_exercise_id))
            Entries.objects.filter(id=complete_exercise_id).update(Additional_Information="Completed")
    exercise = (Exercise.objects.order_by('?').first())
    username="Anonymous"
    fbid=""
    if request.user.is_authenticated:
        username=request.user
        fb = request.user.social_auth.filter(provider='facebook').values('uid').first()
        if fb:
            fbid = fb.get("uid")
    l = Entries(Username=username,
                Tracking="Exercise",
                String_Value=exercise,
                Numerical_Value="60",
                Additional_Information="Skipped",
                fbid=fbid)
    l.save()
    logging.debug('+++ tracker_exercise view +++')
    form = forms.CreateEntry()
    form.initial["Tracking"] = "Exercise"
    today = datetime.now().date()
    logging.debug('todays_date : {}'.format(today))
    entries = Entries.objects.all()\
                              .filter(Username=username,Tracking="Exercise",Date=today)\
                              .exclude(Additional_Information="Skipped")\
                              .order_by('-DateTime')
    entriestable = EntriesTable(entries)

    countdown_number = 60

    # if request.user.is_authenticated:
    #     profile_user = UserProfile.objects.filter(user=request.user)
    #     countdown_number = profile_user[0].countdown_number


    return render(request, 'tracker/tracker_exercise.html', {
            'form': form ,
            'exercise': exercise,
            "exercise_id": l.id,
            'entries_count': Entries.objects.all()
                                      .filter(Username=username,Tracking="Exercise",Date=today)
                                      .exclude(Additional_Information="Skipped")
                                      .count(),
            'exercises_skipped': Entries.objects.all()
                                      .filter(Username=username,Tracking="Exercise",Additional_Information="Skipped")
                                      .count(),
            'entriestable' : entriestable,

            'countdown_number' : countdown_number
        } )

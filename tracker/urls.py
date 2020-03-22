from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'tracker'

urlpatterns = [
    url(r'^dashboard/$'   , views.tracker_dashboard, name="tracker_dashboard"),
    url(r'^exercise/$'    , views.tracker_exercise, name="tracker_exercise"),
    url(r'^profile/$'     , views.tracker_profile, name="tracker_profile"),
    path('', views.index  , name='index'),
]

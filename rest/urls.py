from django.urls import path
from . import views


urlpatterns = [
    path('v1/calendar/init/', views.GoogleCalendarInitView,
         name='Google_Calender_Init'),
    path('v1/calendar/redirect/', views.GoogleCalendarRedirectView,
         name='Google_Calendar_Redirect')
]

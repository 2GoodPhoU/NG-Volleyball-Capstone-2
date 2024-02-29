from django.urls import path
from .views import UserView

urlpatterns = [
    path('User', UserView.as_view()),
    #path('Team', TeamView.as_view()),
    #path('Divisons', DivisonsView.as_view()),
    #path('MatchTable', MatchTableView.as_view()),
    #path('CourtSchedule', CourtScheduleView.as_view())
]
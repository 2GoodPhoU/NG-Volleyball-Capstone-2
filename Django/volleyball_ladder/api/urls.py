from django.urls import path
from .views import UserView, TeamView, DivisonsView, MatchTableView, CourtScheduleView

urlpatterns = [
    path('user', UserView.as_view()),
    path('team', TeamView.as_view()),
    path('divisons', DivisonsView.as_view()),
    path('matchTable', MatchTableView.as_view()),
    path('courtSchedule', CourtScheduleView.as_view())
]
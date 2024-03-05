from django.urls import path
from .views import UserView, TeamView, DivisionView,TeamInDivisionView, MatchTableView, CourtScheduleView

urlpatterns = [
    path('user', UserView.as_view()),
    path('team', TeamView.as_view()),
    path('divisons', DivisionView.as_view()),
    path('matchTable', MatchTableView.as_view()),
    path('courtSchedule', CourtScheduleView.as_view())
]
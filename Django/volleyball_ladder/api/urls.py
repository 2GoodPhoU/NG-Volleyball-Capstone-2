from django.urls import path
from .views import UserView, TeamView, DivisionView,TeamInDivisionView, MatchTableView, CourtScheduleView

urlpatterns = [
    path('User', UserView.as_view()),
    path('Team', TeamView.as_view()),
    path('Division', DivisionView.as_view()),
    path('MatchTable', MatchTableView.as_view()),
    path('CourtSchedule', CourtScheduleView.as_view()),
    path('TeamInDivision',TeamInDivisionView.as_view())
]
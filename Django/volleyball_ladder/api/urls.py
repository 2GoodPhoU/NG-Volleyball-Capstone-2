from django.urls import path
from .views import UserView, TeamView

urlpatterns = [
    path('user', UserView.as_view()),
    path('teams',  TeamView.as_view())
]

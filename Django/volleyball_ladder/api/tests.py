from django.test import TestCase
from .models import User, Team, Division,TeamInDivision, MatchTable, CourtSchedule
from datetime import datetime

#python manage.py test -to run test, it resets every time
#python manage.py flush
class ModelTestCase(TestCase):
    def setUp(self):
        # Create 7 users
        self.user1 = User.objects.create(username='user1', email='user1@example.com', password='password123')
        self.user2 = User.objects.create(username='user2', email='user2@example.com', password='password456')
        self.user3 = User.objects.create(username='user3', email='user3@example.com', password='password789')
        self.user4 = User.objects.create(username='user4', email='user4@example.com', password='password987')
        self.user5 = User.objects.create(username='user5', email='user5@example.com', password='password654')
        self.user6 = User.objects.create(username='user6', email='user6@example.com', password='password321')
        self.user7 = User.objects.create(username='user7', email='user7@example.com', password='password246')

        # Create 2 teams with 3 players each
        self.team1 = Team.objects.create(teamName='Team A', captain=self.user1)
        self.team1.users.add(self.user1, self.user2, self.user3)

        self.team2 = Team.objects.create(teamName='Team B', captain=self.user4)
        self.team2.users.add(self.user4, self.user5, self.user6)

        # Create a division
        self.division = Division.objects.create(name='Division 1', admin=self.user7)
        TeamInDivision.objects.create(division=self.division, team=self.team1, position=1)
        TeamInDivision.objects.create(division=self.division, team=self.team2, position=2)

        # Create a match
        self.match = MatchTable.objects.create(team1Name=self.team1, team2Name=self.team2, ref=self.user7)

        # Create a court schedule for the match
        self.schedule1 = CourtSchedule.objects.create(match=self.match, location='Court 1', startTime=datetime.now(), endTime=datetime.now())
        self.schedule2 = CourtSchedule.objects.create(match=self.match, location='Court 2', startTime=datetime.now(), endTime=datetime.now())
        #Divison
    
    def countCheck_created(self):
        self.assertEqual(User.objects.count(), 7)
        self.assertEqual(Team.objects.count(), 2)
        self.assertEqual(Division.objects.count(), 1)
        self.assertEqual(MatchTable.objects.count(), 1)
        self.assertEqual(CourtSchedule.objects.count(), 2)
        
    def test_select_specific_user(self):
        # Test selecting a specific user by username
        user = User.objects.get(username='user1')
        self.assertEqual(user.username, 'user1')

    def test_select_specific_team(self):
        # Test selecting a specific team by teamName
        team = Team.objects.get(teamName='Team A')
        self.assertEqual(team.teamName, 'Team A')

    def test_select_specific_division(self):
        # Test selecting a specific division by name
        division = Division.objects.get(name='Division 1')
        self.assertEqual(division.name, 'Division 1')

    def test_select_specific_match(self):
        # Test selecting a specific match by teams involved
        match = MatchTable.objects.get(team1Name__teamName='Team A', team2Name__teamName='Team B')
        self.assertEqual(match.team1Name.teamName, 'Team A')
        self.assertEqual(match.team2Name.teamName, 'Team B')

    def test_select_specific_court_schedule(self):
        # Test selecting a specific court schedule by location
        court_schedule = CourtSchedule.objects.get(location='Court 1')
        self.assertEqual(court_schedule.location, 'Court 1')


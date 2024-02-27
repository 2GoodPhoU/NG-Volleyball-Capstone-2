from django.test import TestCase
from .models import User, Team, Divisons, MatchTable, CourtSchedule

#python manage.py test -to run test, it resets every time
#python manage.py flush
class ModelTestCase(TestCase):
    """def setUp(self):
        # Create test data
        self.user = User.objects.create(username='testuser', email='test@example.com', password='password123')
        self.team = Team.objects.create(teamName='Test Team', captain=self.user)
        self.division = Divisons.objects.create(teamName=self.team, position=1, admin=self.user)
        self.match = MatchTable.objects.create(team1Name=self.team, team2Name=self.team)
        self.court_schedule = CourtSchedule.objects.create(location='Court 1', id=self.match)

    def test_user_creation(self):
        # Test user creation
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'test@example.com')

    def test_team_creation(self):
        # Test team creation
        team = Team.objects.get(teamName='Test Team')
        self.assertEqual(team.captain, self.user)
    """
    def CreateUser(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', password='password123')

    def CreateTeam(slef):
        self.team = Team.objects.create(teamName='Test Team', captain='testuser')

    def CreateTeam(slef):
        self.team = Team.objects.create(teamName='Test Team', captain='testuser')

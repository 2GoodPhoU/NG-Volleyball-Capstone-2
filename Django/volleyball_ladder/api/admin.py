from django.contrib import admin
from .models import User
from .models import Team
from .models import Divisons
from .models import MatchTable
from .models import CourtSchedule

# Register your models here.
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Divisons)
admin.site.register(MatchTable)
admin.site.register(CourtSchedule)
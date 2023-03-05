from django.contrib import admin

from stats.models import TeamStat, PlayerBallStat, PlayerBatStat

admin.site.register(TeamStat)
admin.site.register(PlayerBallStat)
admin.site.register(PlayerBatStat)

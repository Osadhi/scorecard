from django.db import models
from django.utils.translation import gettext_lazy as _

from match.models import Match
from team.models import Team, Player


class TeamStat(models.Model):
    created = models.DateTimeField(_('created'), blank=True, editable=False, auto_now_add=True)
    modified = models.DateTimeField(_('modified'), blank=True, editable=False, auto_now=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    total = models.IntegerField(_('total'), null=True, blank=True)
    wickets = models.IntegerField(_('wickets'), null=True, blank=True)
    overs = models.CharField(max_length=10, null=True, blank=True)
    run_rate = models.FloatField(_('run rate'), null=True, blank=True)
    required_run_rate = models.FloatField(_('required run rate'), null=True, blank=True)
    extras = models.IntegerField(_('extras'), null=True, blank=True)
    remaining_balls = models.IntegerField(_('remaining balls'), null=True, blank=True)
    remaining_score = models.IntegerField(_('remaining score'), null=True, blank=True)
    custom_comment = models.TextField(_('custom comment'), blank=True, null=True)

    def __str__(self):
        return self.match.name + ' ' + self.team.name


class PlayerBatStat(models.Model):
    created = models.DateTimeField(_('created'), blank=True, editable=False, auto_now_add=True)
    modified = models.DateTimeField(_('modified'), blank=True, editable=False, auto_now=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    balls = models.IntegerField(_('balls'), null=True, blank=True)
    runs = models.IntegerField(_('runs'), null=True, blank=True)

    def __str__(self):
        return self.match.name + ' ' + self.player.name


class PlayerBallStat(models.Model):
    created = models.DateTimeField(_('created'), blank=True, editable=False, auto_now_add=True)
    modified = models.DateTimeField(_('modified'), blank=True, editable=False, auto_now=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    wickets = models.IntegerField(_('wickets'), null=True, blank=True)
    overs = models.FloatField(_('overs'), null=True, blank=True)
    runs = models.IntegerField(_('runs'), null=True, blank=True)

    def __str__(self):
        return self.match.name + ' ' + self.player.name

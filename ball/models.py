from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from match.models import Round
from stats.models import TeamStat, PlayerBallStat, PlayerBatStat
from team.models import Player


class Over(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    baller = models.ForeignKey(Player, on_delete=models.CASCADE)
    created = models.DateTimeField(_('created'), blank=True, editable=False, auto_now_add=True)
    modified = models.DateTimeField(_('modified'), blank=True, editable=False, auto_now=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('match:detail', args=[str(self.round.match.slug)])

    def ball_count(self):
        return self.ball_set.count()

    def normal_ball_count(self):
        return self.ball_set.filter(ball='-').count() + self.ball_set.filter(ball='B').count()

    def wicket_count(self):
        return self.ball_set.filter(wicket=True).count()

    def runs(self):
        return sum([int(i.score) for i in self.ball_set.filter(ball='-').all()])

    def extras(self):
        return sum([int(i.score) for i in self.ball_set.filter(~Q(ball='-')).all()])

    def total_runs(self):
        return self.runs() + self.extras()


class Ball(models.Model):
    class Score(models.TextChoices):
        NONE = '0', _('None')
        ONE = '1', _('1')
        TWO = '2', _('2')
        THREE = '3', _('3')
        FOUR = '4', _('4')
        FIVE = '5', _('5')
        SIX = '6', _('6')
        SEVEN = '7', _('7')

    class Ball(models.TextChoices):
        NORMAL = '-', _('Normal')
        WIDE = 'WB', _('Wide')
        NO_BALL = 'NB', _('No Ball')
        BYES = 'B', _('Byes')

    over = models.ForeignKey(Over, on_delete=models.CASCADE)
    batsman = models.ForeignKey(Player, on_delete=models.CASCADE)
    wicket = models.BooleanField(default=False)
    score = models.CharField(_('score'), choices=Score.choices, default=Score.NONE, max_length=1)
    ball = models.CharField(_('ball type'), choices=Ball.choices, default=Ball.NORMAL, max_length=2)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('match:detail', args=[str(self.over.round.match.slug)])


@receiver(post_save, sender=Ball)
def update_data(sender, instance, *args, **kwargs):
    match = instance.over.round.match
    round_ = instance.over.round
    team = instance.batsman.team
    batsman = instance.batsman
    baller = instance.over.baller

    defaults_for_team = {'total': round_.total_runs(),
                         'wickets': round_.wicket_count(),
                         'overs': round_.overs_for_card(),
                         'run_rate': round_.run_rate(),
                         'extras': round_.extras()}

    if round_ == match.get_first_round():
        defaults_for_team.update({'remaining_balls': match.remaining_balls_first()})

    elif round_ == match.get_second_round():
        defaults_for_team.update({'remaining_balls': match.remaining_balls_second(),
                                  'required_run_rate': match.required_run_rate(),
                                  'remaining_score': match.remaining_score()})

    TeamStat.objects.update_or_create(match=match, team=team, defaults=defaults_for_team)

    overs_baller = Over.objects.filter(round=round_, baller=baller)

    defaults_for_balling_player = {'overs': overs_baller.count(),
                                   'wickets': sum([i.wicket_count() for i in overs_baller.all()]),
                                   'runs': sum([i.total_runs() for i in overs_baller.all()])}

    PlayerBallStat.objects.update_or_create(match=match, player=baller, defaults=defaults_for_balling_player)

    overs_batsman = round_.over_set.all()

    ball_count = 0
    runs = 0
    for over in overs_batsman:
        ball_count += over.ball_set.filter(batsman=batsman).count()
        runs += sum([int(i.score) for i in over.ball_set.filter(batsman=batsman, ball='-').all()] + \
                    [int(i.score) for i in over.ball_set.filter(batsman=batsman, ball='b').all()])

    defaults_for_batting_player = {'balls': ball_count,
                                   'runs': runs}

    PlayerBatStat.objects.update_or_create(match=match, player=batsman, defaults=defaults_for_batting_player)

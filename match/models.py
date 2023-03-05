from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from scorecard.utils import unique_slug_gen
from team.models import Team

BALLS_PER_OVER = 4
TOTAL_BALLS = BALLS_PER_OVER * 5


class Match(models.Model):
    class Choose(models.TextChoices):
        BAT = 'B', _('Bat')
        FIELD = 'F', _('Field')

    name = models.CharField(max_length=256, null=True)
    slug = models.SlugField(_('slug'), unique=True, blank=True, editable=False)
    created = models.DateTimeField(_('created'), blank=True, editable=False, auto_now_add=True)
    modified = models.DateTimeField(_('modified'), blank=True, editable=False, auto_now=True)
    first_batting = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='first_batting_set', blank=True)
    first_balling = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='first_balling_set', blank=True)
    toss_win = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='toss_win_set')
    elected = models.CharField(_('elected'), choices=Choose.choices, default=Choose.FIELD, max_length=1)
    won = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='won_set', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('match:detail', args=[str(self.slug)])

    def get_first_round(self):
        if self.elected == 'F':
            return self.round_set.filter(balling=self.toss_win).first()
        return self.round_set.filter(batting=self.toss_win).first()

    def get_second_round(self):
        if self.elected == 'F':
            return self.round_set.filter(batting=self.toss_win).first()
        return self.round_set.filter(balling=self.toss_win).first()

    def remaining_score(self):
        first_round_score = self.get_first_round().total_runs()
        second_round_score = self.get_second_round().total_runs()
        if first_round_score >= second_round_score:
            return first_round_score - second_round_score + 1
        return 0

    def remaining_balls_first(self):
        return TOTAL_BALLS - self.get_first_round().normal_ball_count()

    def remaining_balls_second(self):
        return TOTAL_BALLS - self.get_second_round().normal_ball_count()

    def required_run_rate(self):
        if self.remaining_balls_second():
            return round(self.remaining_score() / self.remaining_balls_second() * BALLS_PER_OVER, 2)
        return 0.00

    def team_1(self):
        return self.teamstat_set.filter(team=self.first_batting).first()

    def team_2(self):
        return self.teamstat_set.filter(team=self.first_balling).first()

    def batting_1(self):
        return self.playerbatstat_set.filter(player__team=self.first_batting).all()

    def batting_2(self):
        return self.playerbatstat_set.filter(player__team=self.first_balling).all()

    def balling_1(self):
        return self.playerballstat_set.filter(player__team=self.first_balling).all()

    def balling_2(self):
        return self.playerballstat_set.filter(player__team=self.first_batting).all()


class Round(models.Model):
    name = models.CharField(max_length=256, null=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    batting = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='batting_set')
    balling = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='balling_set')
    created = models.DateTimeField(_('created'), blank=True, editable=False, auto_now_add=True)
    modified = models.DateTimeField(_('modified'), blank=True, editable=False, auto_now=True)

    def __str__(self):
        return self.name

    def current_over(self):
        return self.over_set.order_by('-created').first()

    def over_count(self):
        return self.over_set.count()

    def normal_ball_count(self):
        if self.over_set:
            return sum([i.normal_ball_count() for i in self.over_set.all()])
        return 0

    def total_runs(self):
        if self.over_set:
            return sum([i.total_runs() for i in self.over_set.all()])
        return 0

    def extras(self):
        if self.over_set:
            return sum([i.extras() for i in self.over_set.all()])
        return 0

    def runs(self):
        if self.over_set:
            return sum([i.runs() for i in self.over_set.all()])
        return 0

    def wicket_count(self):
        if self.over_set:
            return sum([i.wicket_count() for i in self.over_set.all()])
        return 0

    def run_rate(self):
        if self.normal_ball_count():
            return round(self.total_runs() / self.normal_ball_count() * BALLS_PER_OVER, 2)
        return 0.00

    def overs_for_card(self):
        return f'{self.normal_ball_count() // BALLS_PER_OVER}.{self.normal_ball_count() % BALLS_PER_OVER}'

    def balling_data(self):
        ballers = self.balling.player_set.all()
        data = []
        for baller in ballers:
            overs = self.over_set.filter(baller=baller)
            if overs.count():
                data.append([baller.name, overs.count(), sum([i.total_runs() for i in overs.all()]),
                             sum([i.wicket_count() for i in overs.all()])])
        return data

    def batting_data(self):
        batsmen = self.batting.player_set.all()
        data = []
        for batsman in batsmen:
            overs = self.over_set.all()
            ball_count = 0
            runs = 0
            for over in overs:
                ball_count += over.ball_set.filter(batsman=batsman).count()
                runs += sum([int(i.score) for i in over.ball_set.filter(batsman=batsman, ball='-').all()] + \
                            [int(i.score) for i in over.ball_set.filter(batsman=batsman, ball='b').all()])
            if ball_count:
                data.append([batsman.name, runs, ball_count])
        return data


@receiver(pre_save, sender=Match)
def unique_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_gen(instance, Match)


@receiver(post_save, sender=Match)
def create_round(sender, instance, *args, **kwargs):
    if not Round.objects.filter(match=instance).count():
        Round.objects.create(name=instance.first_batting.name, match=instance, batting=instance.first_batting,
                             balling=instance.first_balling)
        Round.objects.create(name=instance.first_balling.name, match=instance, batting=instance.first_balling,
                             balling=instance.first_batting)

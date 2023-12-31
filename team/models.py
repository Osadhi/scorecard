from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from scorecard.utils import unique_slug_gen


class Team(models.Model):
    name = models.CharField(max_length=256, default='', blank=True)
    slug = models.SlugField(_('slug'), unique=True, blank=True, editable=False)
    created = models.DateTimeField(
        _('created'), blank=True, editable=False, auto_now_add=True)
    modified = models.DateTimeField(
        _('modified'), blank=True, editable=False, auto_now=True)
    logo = models.ImageField(upload_to='team', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('team:detail', args=[self.slug])


class Player(models.Model):
    name = models.CharField(max_length=256, default='', blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    slug = models.SlugField(_('slug'), unique=True, blank=True, editable=False)
    created = models.DateTimeField(
        _('created'), blank=True, editable=False, auto_now_add=True)
    modified = models.DateTimeField(
        _('modified'), blank=True, editable=False, auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('player:detail', args=[self.slug])


@receiver(pre_save, sender=Team)
def unique_slug_team(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_gen(instance, Team)


@receiver(pre_save, sender=Player)
def unique_slug_player(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_gen(instance, Player)

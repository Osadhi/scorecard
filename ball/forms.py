from django import forms
from django.forms import ModelForm

from ball.models import Over, Ball
from team.models import Player


class OverCreateForm(ModelForm):
    class Meta:
        model = Over
        fields = ['baller']

    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team')
        super().__init__(*args, **kwargs)
        self.fields['baller'] = forms.ModelChoiceField(
            queryset=Player.objects.filter(team=team))


class BallCreateForm(ModelForm):
    class Meta:
        model = Ball
        fields = ['batsman', 'wicket', 'score', 'ball']

    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team')
        super().__init__(*args, **kwargs)
        self.fields['batsman'] = forms.ModelChoiceField(
            queryset=Player.objects.filter(team=team))
        self.fields['wicket'] = forms.BooleanField(required=False)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from ball.forms import OverCreateForm, BallCreateForm
from .models import Match


class MatchCreateView(LoginRequiredMixin, CreateView):
    model = Match
    template_name = 'match/create.html'
    fields = ['name', 'toss_win', 'elected', 'first_batting', 'first_balling', 'overs', 'ball_per_over']


class MatchListView(LoginRequiredMixin, ListView):
    model = Match
    template_name = "match/list.html"


class MatchDetailView(LoginRequiredMixin, DetailView):
    model = Match
    template_name = "match/detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form_over_1'] = OverCreateForm(team=self.object.first_balling)
        data['form_over_2'] = OverCreateForm(team=self.object.first_batting)
        data['form_ball_1'] = BallCreateForm(team=self.object.first_batting)
        data['form_ball_2'] = BallCreateForm(team=self.object.first_balling)
        return data


class MatchScoreboardView(DetailView):
    model = Match
    template_name = "match/board.html"


class MatchDeleteView(LoginRequiredMixin, DeleteView):
    model = Match
    template_name = "match/delete.html"
    success_url = reverse_lazy('match:list')


class MatchUpdateView(LoginRequiredMixin, UpdateView):
    model = Match
    template_name = "match/update.html"
    fields = ['name', 'toss_win', 'elected', 'first_batting', 'first_balling', 'won', 'overs', 'ball_per_over',
              'custom_comment']

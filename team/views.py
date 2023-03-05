from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from team.models import Team, Player


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    template_name = 'team/create.html'
    fields = '__all__'


class TeamListView(LoginRequiredMixin, ListView):
    model = Team
    template_name = "team/list.html"


class TeamDetailView(LoginRequiredMixin, DetailView):
    model = Team
    template_name = "team/detail.html"


class TeamDeleteView(LoginRequiredMixin, DeleteView):
    model = Team
    template_name = "team/delete.html"
    success_url = reverse_lazy('team:list')


class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = Team
    template_name = "team/update.html"
    fields = '__all__'


class PlayerCreateView(LoginRequiredMixin, CreateView):
    model = Player
    template_name = 'player/create.html'
    fields = '__all__'


class PlayerListView(LoginRequiredMixin, ListView):
    model = Player
    template_name = "player/list.html"


class PlayerDetailView(LoginRequiredMixin, DetailView):
    model = Player
    template_name = "player/detail.html"


class PlayerDeleteView(LoginRequiredMixin, DeleteView):
    model = Player
    template_name = "player/delete.html"
    success_url = reverse_lazy('player:list')


class PlayerUpdateView(LoginRequiredMixin, UpdateView):
    model = Player
    template_name = "player/update.html"
    fields = '__all__'

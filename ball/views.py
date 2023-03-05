from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from ball.models import Over, Ball
from match.models import Round


class OverCreateView(LoginRequiredMixin, CreateView):
    model = Over
    template_name = 'over/create.html'
    fields = ['baller']

    def form_valid(self, form):
        round_id = self.request.POST.get('round')
        if round_id:
            form.instance.round = Round.objects.get(id=round_id)
        return super().form_valid(form)


class BallCreateView(LoginRequiredMixin, CreateView):
    model = Ball
    template_name = 'over/b_create.html'
    fields = ['batsman', 'wicket', 'score', 'ball']

    def form_valid(self, form):
        over_id = self.request.POST.get('over')
        if over_id:
            form.instance.over = Over.objects.get(id=over_id)
        return super().form_valid(form)

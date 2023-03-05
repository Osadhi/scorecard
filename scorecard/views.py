from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import ListView

from match.models import Match


class SigninView(LoginView):
    template_name = 'accounts/signin.html'
    redirect_authenticated_user = True


def index(request):
    return render(request, 'index.html', context={"request": request})


class MatchListView(ListView):
    model = Match
    template_name = "match/list2.html"

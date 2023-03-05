from django.urls import path

from .views import MatchCreateView, MatchListView, MatchDetailView, MatchUpdateView, MatchDeleteView, \
    MatchScoreboardView

app_name = 'match'
urlpatterns = [
    path('', MatchListView.as_view(), name='list'),
    path('create', MatchCreateView.as_view(), name='create'),
    path('<slug:slug>', MatchScoreboardView.as_view(), name='scoreboard'),
    path('<slug:slug>/detail', MatchDetailView.as_view(), name='detail'),
    path('<slug:slug>/update', MatchUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete', MatchDeleteView.as_view(), name='delete'),
]

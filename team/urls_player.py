from django.urls import path

from .views import PlayerCreateView, PlayerListView, PlayerDetailView, PlayerUpdateView, PlayerDeleteView

app_name = 'player'
urlpatterns = [
    path('', PlayerListView.as_view(), name='list'),
    path('create', PlayerCreateView.as_view(), name='create'),
    path('<slug:slug>/', PlayerDetailView.as_view(), name='detail'),
    path('<slug:slug>/update', PlayerUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete', PlayerDeleteView.as_view(), name='delete'),
]

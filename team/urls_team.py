from django.urls import path

from .views import TeamCreateView, TeamListView, TeamDetailView, TeamUpdateView, TeamDeleteView

app_name = 'team'
urlpatterns = [
    path('', TeamListView.as_view(), name='list'),
    path('create', TeamCreateView.as_view(), name='create'),
    path('<slug:slug>/', TeamDetailView.as_view(), name='detail'),
    path('<slug:slug>/update', TeamUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete', TeamDeleteView.as_view(), name='delete'),
]

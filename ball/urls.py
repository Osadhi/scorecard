from django.urls import path

from .views import OverCreateView, BallCreateView

app_name = 'over'
urlpatterns = [
    path('create', OverCreateView.as_view(), name='create'),
    path('ball/create', BallCreateView.as_view(), name='b_create'),
]

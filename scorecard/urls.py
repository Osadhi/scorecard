"""scorecard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from scorecard.views import SigninView, MatchListView

urlpatterns = [
    path('', MatchListView.as_view(), name='match-list'),
    path('admin/', admin.site.urls),
    path('match/', include('match.urls')),
    path('over/', include('ball.urls')),
    path('team/', include('team.urls_team')),
    path('player/', include('team.urls_player')),
    path('signin', SigninView.as_view(), name='signin'),
    path('signout', LogoutView.as_view(), name='signout'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

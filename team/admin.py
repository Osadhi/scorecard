from django.contrib import admin

from .models import Team, Player


@admin.register(Team)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Player)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

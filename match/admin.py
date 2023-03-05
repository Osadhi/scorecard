from django.contrib import admin

from .models import Match, Round

admin.site.register(Match)


@admin.register(Round)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

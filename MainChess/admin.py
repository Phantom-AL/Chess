from django.contrib import admin
from .models import Players, Tournament, Participant


@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'rating', 'profile_link')


admin.site.register(Tournament)
admin.site.register(Participant)


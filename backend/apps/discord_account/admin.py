from django.contrib import admin

from discord_account.models import DiscordAccount


@admin.register(DiscordAccount)
class DiscordAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password')
    list_display_links = ('username',)

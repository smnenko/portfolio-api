from graphene_django import DjangoObjectType

from discord_account.models import DiscordAccount


class DiscordAccountType(DjangoObjectType):
    class Meta:
        model = DiscordAccount
        fields = ('id', 'username', 'email', 'password')

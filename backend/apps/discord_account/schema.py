import graphene

from discord_account.models import DiscordAccount
from discord_account.types import DiscordAccountType


class Query(graphene.ObjectType):
    discord_accounts = graphene.List(DiscordAccountType)

    def resolve_discord_accounts(self, info, *args, **kwargs):
        return DiscordAccount.objects.all()


schema = graphene.Schema(query=Query)

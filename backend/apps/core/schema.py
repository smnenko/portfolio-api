import graphene
import graphql_jwt

from discord_account.schema import Query as DiscordAccountQuery
from mail_account.schema import Query as MailAccountQuery

from apps.mail_account.schema import CreateAccount as CreateMailAccount
from apps.mail_account.schema import PassCaptchaAnswer as PassCaptchaAnswer


class Query(
    DiscordAccountQuery,
    MailAccountQuery,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    create_mail_account = CreateMailAccount.Field()
    pass_captcha_answer = PassCaptchaAnswer.Field()

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

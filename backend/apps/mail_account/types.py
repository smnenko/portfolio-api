from graphene_django import DjangoObjectType

from mail_account.models import MailAccount


class MailAccountType(DjangoObjectType):
    class Meta:
        model = MailAccount
        fields = ('id', 'email', 'password', 'secret_answer')

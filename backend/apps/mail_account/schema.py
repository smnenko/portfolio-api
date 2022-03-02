import graphene
from django.core.cache import cache

from mail_account.models import MailAccount
from mail_account.types import MailAccountType

from apps.mail_account.utils import MailCreationUtil


class Query(graphene.ObjectType):
    mail_accounts = graphene.List(MailAccountType)
    captcha = graphene.String(user=graphene.String())

    @staticmethod
    def resolve_mail_accounts(root, info, *args, **kwargs):
        return MailAccount.objects.all()

    @staticmethod
    def resolve_captcha(root, info, user, *args, **kwargs):
        return cache.get(f'{user}')


class CreateAccount(graphene.Mutation):
    class Arguments:
        user = graphene.String()

    email = graphene.String()
    password = graphene.String()
    secret_answer = graphene.String()

    @staticmethod
    def mutate(root, info, user: str):
        mail = MailCreationUtil()
        gen = mail.create_account()
        captcha_img_url = gen.send(None)
        cache.set(f'{user}', f'{captcha_img_url}', timeout=120)
        while not cache.get(f'{captcha_img_url}'):
            pass

        try:
            captcha_answer = cache.get(f"{captcha_img_url}")
            gen.send(captcha_answer)
        except StopIteration as e:
            print(f'{e=}')
            return CreateAccount(email=e[0], password=e[1], secret_answer=e[2])


class PassCaptchaAnswer(graphene.Mutation):
    class Arguments:
        captcha = graphene.String()
        answer = graphene.String()

    status = graphene.String()

    @staticmethod
    def mutate(root, info, captcha: str, answer: str):
        cache.set(f'{captcha}', f'{answer}', timeout=120)
        return PassCaptchaAnswer(status='Success')


schema = graphene.Schema(query=Query)

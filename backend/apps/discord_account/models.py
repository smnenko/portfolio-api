from django.db import models

from core.models import AbstractModel
from mail_account.models import MailAccount


class DiscordAccount(AbstractModel):
    email = models.OneToOneField(to=MailAccount, on_delete=models.CASCADE)
    username = models.CharField(max_length=72)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.username}'

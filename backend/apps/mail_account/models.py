from django.db import models

from core.models import AbstractModel


class MailAccount(AbstractModel):
    email = models.EmailField(max_length=46)
    password = models.CharField(max_length=32)
    secret_answer = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.email}'

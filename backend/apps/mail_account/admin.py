from django.contrib import admin

from mail_account.models import MailAccount


@admin.register(MailAccount)
class MailAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'password', 'secret_answer')
    list_display_links = ('email', )

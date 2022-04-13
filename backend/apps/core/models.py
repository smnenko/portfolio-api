from django.db import models
from django.utils import timezone


class AbstractModel(models.Model):
    id = models.IntegerField(primary_key=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(args, kwargs)

    def delete(self, *args, **kwargs):
        self.is_active = False
        super().save(update_fields=('is_active',))

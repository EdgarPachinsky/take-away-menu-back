from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class AbstractBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(_('Last Update'), auto_now_add=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.modified = timezone.now()
        return super().save(*args, **kwargs)

"""Models."""

from django.db import models


class Label(models.Model):
    name = models.CharField(verbose_name='name',
                            max_length=50,
                            unique=True,
                            blank=False,
                            null=False)
    created_at = models.DateField(verbose_name='created at',
                                  auto_now=True,
                                  editable=False)

    def __str__(self):
        return self.name

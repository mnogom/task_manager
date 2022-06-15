"""Models."""

from django.db import models


class Status(models.Model):
    name = models.CharField(verbose_name='name',
                            max_length=300,
                            unique=True,
                            blank=False,
                            null=False)
    description = models.TextField(verbose_name='description',
                                   blank=True,
                                   null=False)
    created_at = models.DateField(verbose_name='created at',
                                  auto_now_add=True,
                                  editable=False)

    def __str__(self):
        return self.name

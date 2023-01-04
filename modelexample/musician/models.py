from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    name = models.CharField(_("Name"), max_length=128)

    def __str__(self) -> str:
        return self.name


class Group(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    members = models.ManyToManyField("Person", verbose_name=_("Members"), through="Membership")

    def __str__(self) -> str:
        return self.name


class Membership(models.Model):
    person = models.ForeignKey("Person", verbose_name=_("Person"), on_delete=models.CASCADE)
    group = models.ForeignKey("Group", verbose_name=_("Group"), on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

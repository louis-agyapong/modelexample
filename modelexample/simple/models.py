from django.db import models
from django.utils.translation import gettext_lazy as _


class Language(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    def __str__(self) -> str:
        return self.name


class Framework(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    language = models.ForeignKey(Language, verbose_name=_("Language"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    def __str__(self) -> str:
        return self.name


class Character(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    movies = models.ManyToManyField("Movie", verbose_name=_("Movies"))

    def __str__(self) -> str:
        return self.name
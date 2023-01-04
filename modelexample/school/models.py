from django.db import models
from django.utils.translation import gettext_lazy as _


# class Student(models.Model):
#     name = models.CharField(_("Name"), max_length=255)

#     def __str__(self) -> str:
#         return self.name


# class Course(models.Model):
#     name = models.CharField(_("Name"), max_length=255)
#     students = models.ManyToManyField("Student", verbose_name=_("Students"))

#     def __str__(self) -> str:
#         return self.name

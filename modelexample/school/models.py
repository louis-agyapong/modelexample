from django.db import models
from django.utils.translation import gettext_lazy as _


class Student(models.Model):
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    students = models.ManyToManyField("Student", verbose_name=_("Students"), through="Enrollment")

    def __str__(self) -> str:
        return self.name


class Enrollment(models.Model):
    class Grades(models.TextChoices):
        A = "A", _("A")
        B = "B", _("B")
        C = "C", _("C")

    student = models.ForeignKey("Student", verbose_name=_("Student"), on_delete=models.CASCADE)
    course = models.ForeignKey("Course", verbose_name=_("Course"), on_delete=models.CASCADE)
    date_enrolled = models.DateField(_("Date Enrolled"))
    final_grade = models.CharField(
        _("Final Grade"),
        max_length=1,
        blank=True,
        default="",
        choices=Grades.choices,
    )

    class Meta:
        constraints = [models.UniqueConstraint(name="unique_student_course", fields=["student", "course"])]

    def __str__(self) -> str:
        return f"{self.student.name} -- {self.course.name}"

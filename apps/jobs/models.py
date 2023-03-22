from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.commons.models import TimeStampedUUIDModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Job(TimeStampedUUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_("Job Title"), max_length=255)
    description = models.TextField()
    qualifications = models.TextField()
    min_salary = models.DecimalField(max_digits=10, decimal_places=2)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2)
    application_details = models.TextField()

    def __str__(self):
        return self.title

    @property
    def get_salary_range(self):
        return f"{self.min_salary} - {self.max_salary}"

    def get_absolute_url(self):
        return reverse("job:job_detail", kwargs={"pkid": self.pkid})

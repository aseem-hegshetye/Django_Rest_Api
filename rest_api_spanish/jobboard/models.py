from django.db import models


class JobBoard(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=100)
    job_description = models.CharField(max_length=100)
    salary = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name

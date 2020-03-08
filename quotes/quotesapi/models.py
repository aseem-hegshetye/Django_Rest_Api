from django.db import models


class Quote(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()
    context = models.CharField(max_length=200, blank=True)
    source = models.CharField(max_length=200, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} -- {self.body}'

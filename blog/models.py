from django.db import models

# Create your models here.


class blogForm(models.Model):
    name = models.CharField(max_length = 120, blank = False)
    email = models.CharField(max_length=120, blank=False, null = False)
    numberPhone = models.CharField(max_length=31, blank=True)
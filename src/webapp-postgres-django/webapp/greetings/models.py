from django.db import models

# Create your models here.
class Words(models.Model):
    lang = models.CharField(max_length=3, null=False, blank=False)
    word = models.CharField(max_length=50, null=False, blank=False)

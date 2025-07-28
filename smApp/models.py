from django.db import models


# Create your models here.
class schoolInfo(models.Model):
    schoolName = models.CharField(max_length=200)
    schoolAddress = models.CharField(max_length=200)
    schoolEstablished = models.IntegerField()
    schoolEstablisher = models.CharField(max_length=200, blank=True, null=True)

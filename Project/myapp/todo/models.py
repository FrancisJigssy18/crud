from django.db import models

# Create your models here.
class ListModel(models.Model):
    text = models.CharField(max_length=250, null=False, blank=False)

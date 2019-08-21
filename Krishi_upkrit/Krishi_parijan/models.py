from django.db import models

# Create your models here.
class MPN(models.Model):
    mac = models.CharField(max_length=30)
    available = models.BoolField(max_length=30)

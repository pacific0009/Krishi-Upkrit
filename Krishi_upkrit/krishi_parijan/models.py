from django.db import models

# Create your models here.
class MPNTable(models.Model):
    mac = models.CharField(max_length=30)
    available = models.BooleanField()
    last_active = models.DateTimeField()


class MPNRoutingTable(models.Model):
    destination = models.IntegerField()
    distance = models.IntegerField()
    next_hop = models.IntegerField()
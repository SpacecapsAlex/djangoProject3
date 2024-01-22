from django.db import models

from example.models import User


# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    lead_name = models.CharField(max_length=100)
    count_users = models.IntegerField()
    # Связь многие ко многи с таблицей User
    users = models.ManyToManyField(User)

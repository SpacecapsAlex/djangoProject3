from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    birthday = models.DateField()
    description = models.TextField(null=True, blank=True)


# Связь один ко многим
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Связь один к одному
class Comment(models.Model):
    text = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

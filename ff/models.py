from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class FicType(models.Model):
    name = models.CharField(max_length=6)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.user.email


class Fic(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.ForeignKey(FicType, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    latest = models.IntegerField(null=True)
    fandom = models.CharField(max_length=100)

    def __str__(self):
        return self.title + " (" + str(self.id) + ")"


class MyFic(models.Model):
    fic = models.ForeignKey(Fic, on_delete=models.CASCADE)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    current = models.IntegerField(null=True)
    up_to_date = models.BooleanField()
    notes = models.CharField(max_length=200)

    def __str__(self):
        return self.fic.title + " (" + str(self.fic.id) + ") " + self.user.user.email

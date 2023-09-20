from django.db import models


class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author="Roald Dahl")


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    objects = models.Manager()
    dahl_objects = DahlBookManager()


class Reporters(models.Model):
    name = models.CharField(max_length=255)
    stories_filed = models.IntegerField()

    def __str__(self):
        return self.name

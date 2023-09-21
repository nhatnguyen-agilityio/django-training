from django.db import models
from datetime import datetime


class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author="Roald Dahl")


class BookAuthor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
    pages = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rating = models.FloatField(default=5)
    authors = models.ManyToManyField(BookAuthor)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, null=True, blank=True
    )
    pubdate = models.DateField(default=datetime.now())
    objects = models.Manager()
    dahl_objects = DahlBookManager()

    def __str__(self):
        return self.title


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)


class Reporters(models.Model):
    name = models.CharField(max_length=255)
    stories_filed = models.IntegerField()

    def __str__(self):
        return self.name

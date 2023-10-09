from django.db import models


class Students(models.Model):
    name = models.CharField(
        verbose_name="Student name", help_text="Enter the student name here"
    )
    age = models.PositiveIntegerField()
    address = models.CharField(default="Da Nang")
    email = models.EmailField(verbose_name="Email address")
    birthday = models.DateField()
    note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "list_students"
        verbose_name = "List Students"
        ordering = ["birthday"]


class Class(models.Model):
    class_name = models.CharField(max_length=10)
    students = models.ForeignKey(Students, on_delete=models.CASCADE)
    note = models.TextField(blank=True, null=True, max_length=255)

    class Meta:
        order_with_respect_to = "students"


class Car(models.Model):
    car_name = models.CharField(max_length=255)
    note = models.TextField(blank=True, null=True)
    manufacture = models.DateField()

    class Meta:
        models.Index(fields=["car_name", "-manufacture"])

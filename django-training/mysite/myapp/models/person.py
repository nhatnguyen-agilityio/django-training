from django.db import models


class Person(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    first_name = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="The first name"
    )
    last_name = models.CharField(max_length=30, verbose_name="The last name")
    birth_date = models.DateField()
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return self.first_name + self.last_name

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime

        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{self.first_name} {self.last_name}"


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


class Manufactures(models.Model):
    pass


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufactures, on_delete=models.CASCADE)

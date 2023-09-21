from django.db import models


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(quantity__gt=0)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField()
    discount_price = models.PositiveBigIntegerField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    objects = models.Manager()
    product_stock = ProductManager()

    def __str__(self):
        return self.name


class Order(models.Model):
    email = models.EmailField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.email

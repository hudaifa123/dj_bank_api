from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    """
    Currency model class for storing currency information in the database using the currency service
    """

    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Category model class for category models that have a category attribute defined
    """

    user = models.ForeignKey(User, related_name="categories", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    """
    A transaction is a series of operations that are performed in a transaction.
    """

    user = models.ForeignKey(User, related_name="transactions", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=104, decimal_places=5)
    currency = models.ForeignKey(Currency, related_name="transactions", on_delete=models.PROTECT)
    category = models.ForeignKey(Category, related_name="transactions", on_delete=models.SET_NULL, blank=True, null=True)
    descriptions = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

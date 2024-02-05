from utils.model_base import BaseModel
from django.db import models
from user.models import UserAccount

from django.utils import timezone


class ProductPrice(BaseModel):
    CURRENCIES = (
        ("PLN", "PLN"),
        ("EUR", "EUR"),
        ("USD", "USD"),
    )

    value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCIES)
    price_id = models.CharField(max_length=250, unique=True)
    
    class Meta:
        verbose_name = "Product price"
        verbose_name_plural = "Product prices"

    def __str__(self):
        return f"{self.value} {self.currency}"


class Product(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.ManyToManyField(ProductPrice)
    max_project_storage = models.PositiveIntegerField()
    num_of_projects = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_free = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name}"


class UserSubscription(BaseModel):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    expiration_date = models.DateTimeField()

    class Meta:
        verbose_name = "User subscription"
        verbose_name_plural = "User subscriptions"

    def __str__(self):
        return f"{self.user} {self.product.name}"

    @property
    def is_expired(self):
        return self.expiration_date < timezone.now()

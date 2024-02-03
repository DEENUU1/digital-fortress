from utils.model_base import BaseModel
from django.db import models


class ProductPrice(BaseModel):
    CURRENCIES = (
        ("PLN", "PLN"),
        ("EUR", "EUR"),
        ("USD", "USD"),
    )

    BILLING_CYCLES = (
        ("1", "monthly"),
        ("2", "life time")
    )

    value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCIES)
    price_id = models.CharField(max_length=250, unique=True)
    billing_cycle = models.CharField(max_length=2, choices=BILLING_CYCLES)

    class Meta:
        verbose_name = "Product price"
        verbose_name_plural = "Product prices"

    def __str__(self):
        return f"{self.value} {self.currency} {self.billing_cycle}"


class Product(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.ManyToManyField(ProductPrice)
    max_project_storage = models.PositiveIntegerField()
    num_of_projects = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name}"

from django.db import models
from django.contrib.auth.models import User
from typing import TYPE_CHECKING
from django.db.models import Manager


def preview_location(instance: "Product", filename: str) -> str:
    return "products/product_{pk}/preview/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Product(models.Model):
    class Meta:
        ordering = ['name', 'price']
    name = models.CharField(max_length=50)
    description = models.TextField(null=False, blank=True, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    preview = models.ImageField(null=True, blank=True, upload_to='preview_location')

    def __str__(self):
        return f"Product(pk={self.pk}, name: {self.name!r})"

    if TYPE_CHECKING:
        object: Manager


def product_images_location(instance: "ProductImage", filename: str) -> str:
    return "products/product_{pk}/images/{filename}".format(
        pk=instance.product.pk,
        filename=filename,
    )


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=product_images_location)
    description = models.CharField(max_length=200, null=False, blank=True)


class Order(models.Model):
    delivery_address = models.TextField(null=True, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')
    receipt = models.FileField(null=True, upload_to="orders/receipts/")

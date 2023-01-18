from django.db import models
from django.urls import reverse
from django.utils import timezone

from accounts.models import Customer


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.00)
    stock = models.IntegerField(default=0)
    slug = models.CharField(max_length=100, name="slug", blank=False, null=False)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('store:product_detail', kwargs={'slug': self.slug})


class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.product.name} - {self.user.username} - {self.quantity} "


class Cart(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order, related_name="Cart_Orders")

    def __str__(self) -> str:
        return f"{self.user.username} - {self.ordered} - {self.ordered_date}"

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        self.orders.clear()

        super().delete(*args, **kwargs)

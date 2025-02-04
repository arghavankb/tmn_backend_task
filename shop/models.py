from django.db import models
from django.core.validators import MinValueValidator
from shop.validators import validate_image_size


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField()

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(
        upload_to="shop/images",
        validators=[validate_image_size]
    )

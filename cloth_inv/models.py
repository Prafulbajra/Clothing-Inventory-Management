from django.db import models


# Create your models here.
class Cloth(models.Model):
    class Category(models.TextChoices):
        SHIRT = ("SH", "Shirt")
        PANT = ("PT", "Pant")
        T_SHIRT = ("TS", "T-Shirt")
        SUIT = ("ST", "Suit")
        INNERWEAR = ("IW", "Innerwear")

    class Size(models.TextChoices):
        SMAll = ("S", "S")
        MEDIUM = ("M", "M")
        LARGE = ("L", "L")
        EXTRA_LARGE = ("XL", "XL")
        EXTRA_EXTRA_LARGE = ("XXL", "XXL")

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=3,
        choices=Category.choices,
    )
    size = models.CharField(
        max_length=3,
        choices=Size.choices,
        default=Size.LARGE,
    )
    color = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    stock = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

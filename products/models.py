from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    slug = models.SlugField(null=False)
    price = models.FloatField(default=0)
    description = RichTextField()
    owner = models.ForeignKey(
        get_user_model(),
        related_name="sold_products",
        on_delete=models.CASCADE,
        verbose_name="owner",
    )
    customers = models.ManyToManyField(
        "users.User",
        related_name="bought_products",
        verbose_name="customers",
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

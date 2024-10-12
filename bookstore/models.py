from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator
from django.urls import reverse
from django.utils.text import slugify

class Book(models.Model):
    # id = models.AutoField() -> implemented by django
    title = models.CharField(max_length=25)
    author = models.CharField(null=True, max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxLengthValidator(10)])
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def __str__(self):
        # in every class
        return f"Title: {self.title}, Rating: {self.rating}"
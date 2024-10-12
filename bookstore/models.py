from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator

class Book(models.Model):
    # id = models.AutoField() -> implemented by django
    title = models.CharField(max_length=25)
    author = models.CharField(null=True, max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxLengthValidator(10)])
    is_bestselling = models.BooleanField(default=False)

    def __str__(self):
        # in every class
        return f"Title: {self.title}, Rating: {self.rating}"
from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    option=(
        ("novel","novel"),
        ("stories","stories"),
        ("articles","articles"),
        ("biopic","biopic")
    )
    category = models.CharField(max_length=200,choices=option)
    language = models.CharField(max_length=200,null=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

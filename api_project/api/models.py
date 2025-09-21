from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)   # a short text field
    author = models.CharField(max_length=100)  # another short text field

    def __str__(self):
        return self.title


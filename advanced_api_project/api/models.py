from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)  # string field for author name

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)  # string field for book title
    publication_year = models.IntegerField()  # integer field for year published
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"  # allows reverse lookup: author.books.all()
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


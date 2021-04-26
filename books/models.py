from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books:view_author', kwargs={'pk': self.pk})


class Book(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.ForeignKey('Author', null=False, blank=False,
                on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

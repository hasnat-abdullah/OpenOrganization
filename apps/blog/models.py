from django.db import models
from apps.organization_details.models import BaseModel
import os


class Category(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='blog/author/', default=None)
    fb_url = models.URLField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name


class Articles(BaseModel):
    title = models.CharField(max_length=249)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='blog/thumb/')
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.title


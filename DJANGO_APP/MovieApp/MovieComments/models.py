from django.db import models

# Create your models here.

class Movie(models.Model):
    movie = models.CharField(max_length=150)
    comment = models.TextField()
    sentiment = models.CharField(max_length = 10)
    header_urls = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
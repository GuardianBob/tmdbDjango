from django.db import models

class CheckMovie(models.Manager):
    def validate_review(self, postData):
        errors = {}
        pass

class Movie(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CheckMovie()

# Create your models here.

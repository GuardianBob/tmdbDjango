from django.db import models
from loginApp.models import User

class CheckMovie(models.Manager):
    def validate_review(self, postData):
        errors = {}
        pass

class Movie(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    watch_later = models.ForeignKey(User, related_name='watching', on_delete=models.CASCADE)
    favorite = models.ManyToManyField(User, related_name="favorites", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CheckMovie()

# Create your models here.

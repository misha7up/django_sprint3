from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=False)
    slug = models.SlugField(unique=True, blank=False)
    is_published = models.BooleanField(default=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)


class Location(models.Model):
    name = models.CharField(max_length=256, blank=False)
    is_published = models.BooleanField(default=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)


class Post(models.Model):
    title = models.CharField(max_length=256, blank=False)
    text = models.TextField(blank=False)
    pub_date = models.DateTimeField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,
                                 null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 blank=False, null=True)
    is_published = models.BooleanField(default=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)

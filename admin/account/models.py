from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class UsersInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        db_table = 'users'


class Cards(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField(null=True)
    user = models.ForeignKey(UsersInfo, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('card:carddetail', args=[self.slug])

    class Meta:
        db_table = 'cards'
        ordering = ['-published']

    def __str__(self):
        return self.title

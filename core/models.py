from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE, 
        related_name='profile'
    )
    
    def __str__(self):
        return self.user.username


class News(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255) 
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0)
    is_publicated = models.BooleanField(default=True)
    img = models.ImageField(upload_to='news', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['title']


class Advice(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255) 
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0)
    is_publicated = models.BooleanField(default=True)
    img = models.ImageField(upload_to='news', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Совет'
        verbose_name_plural = 'Советы'
        ordering = ['title']
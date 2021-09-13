from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, 
        null=True, blank=True
    )
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255) #короткое описание
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    is_publicated = models.BooleanField(default=True)
    img = models.ImageField(upload_to='recipes', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['name']

class Feedback(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Пользователь'
    
    )

    recipe = models.ForeignKey(
        to=Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )

    text = models.TextField(
        verbose_name='Текст обратной связи'
    )

    checked = models.BooleanField(default=False, verbose_name='Обработано')

    def __str__(self):
        return self.text[:20]

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    author_name = models.CharField('автор', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

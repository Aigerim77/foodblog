from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE, 
        related_name='profile'
    )

    level = models.CharField(max_length=15, choices=(
        ('Шеф-повар', 'Шеф-повар'),
        ('Повар', 'Повар'),
        ('Любитель', 'Любитель'),
        ('Домохозяйка', 'Домохозяйка'),
    ))

    photo = models.ImageField(
        upload_to='profile_photo',
        null=True, blank=True
    )

    def __str__(self):
        return self.user.username
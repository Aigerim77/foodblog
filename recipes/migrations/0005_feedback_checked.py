# Generated by Django 3.2.6 on 2021-08-12 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='checked',
            field=models.BooleanField(default=False, verbose_name='Обработано'),
        ),
    ]
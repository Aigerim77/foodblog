# Generated by Django 3.2.7 on 2021-09-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20210914_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='news',
            name='user',
        ),
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-13 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]

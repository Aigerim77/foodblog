# Generated by Django 3.2.6 on 2021-08-10 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_profile_type_of_dish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='type_of_dish',
        ),
    ]
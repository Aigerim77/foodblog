# Generated by Django 3.2.6 on 2021-08-11 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_profile_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.CharField(choices=[('Шеф-повар', 'Ш'), ('Повар', 'П'), ('Любитель', 'Л'), ('Домохозяйка', 'Д')], max_length=15),
        ),
    ]
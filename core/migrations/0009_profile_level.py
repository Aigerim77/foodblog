# Generated by Django 3.2.6 on 2021-08-11 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_profile_type_of_dish'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.CharField(choices=[('Ш', 'Шеф-повар'), ('П', 'Повар'), ('Л', 'Любитель'), ('Д', 'Домохозяйка')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.1.5 on 2021-02-05 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210204_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimmer',
            name='swimmer_id',
            field=models.CharField(max_length=7),
        ),
    ]
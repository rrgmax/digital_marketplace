# Generated by Django 2.1.5 on 2019-02-22 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190221_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
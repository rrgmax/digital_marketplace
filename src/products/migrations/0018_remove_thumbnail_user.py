# Generated by Django 2.1.5 on 2019-02-28 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20190227_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='user',
        ),
    ]

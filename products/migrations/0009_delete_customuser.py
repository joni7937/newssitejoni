# Generated by Django 4.2.5 on 2023-10-19 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-12 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_categorymodel_productmodel_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]

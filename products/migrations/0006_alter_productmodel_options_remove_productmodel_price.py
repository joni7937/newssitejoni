# Generated by Django 4.2.5 on 2023-10-15 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_categorymodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productmodel',
            options={'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='price',
        ),
    ]

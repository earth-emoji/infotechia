# Generated by Django 2.2.13 on 2020-07-13 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20191027_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'verbose_name': 'thread', 'verbose_name_plural': 'threads'},
        ),
    ]
# Generated by Django 3.2.3 on 2021-05-30 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210530_1410'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Simple_Book',
            new_name='Book',
        ),
    ]
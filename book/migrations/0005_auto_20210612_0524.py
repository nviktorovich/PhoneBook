# Generated by Django 3.2.3 on 2021-06-12 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20210612_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplebook',
            name='phone1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='simplebook',
            name='phone2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='simplebook',
            name='phone3',
            field=models.IntegerField(null=True),
        ),
    ]
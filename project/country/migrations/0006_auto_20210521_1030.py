# Generated by Django 3.1.7 on 2021-05-21 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0005_auto_20210513_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='population',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
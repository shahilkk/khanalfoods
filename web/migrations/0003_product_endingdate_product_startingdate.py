# Generated by Django 4.1.3 on 2022-11-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_customer_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='endingdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='startingdate',
            field=models.DateField(auto_now=True),
        ),
    ]

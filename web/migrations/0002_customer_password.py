# Generated by Django 4.1.3 on 2022-11-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.1.3 on 2021-01-24 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210123_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
    ]

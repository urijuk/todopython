# Generated by Django 3.1.3 on 2021-01-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_book_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.2.8 on 2024-04-26 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0004_recipes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='recommendation',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

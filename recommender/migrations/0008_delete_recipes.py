# Generated by Django 4.2.8 on 2024-04-27 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0007_alter_post_created_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recipes',
        ),
    ]
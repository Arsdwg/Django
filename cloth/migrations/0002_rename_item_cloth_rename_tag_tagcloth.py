# Generated by Django 5.0.4 on 2024-05-13 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cloth", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Item",
            new_name="Cloth",
        ),
        migrations.RenameModel(
            old_name="Tag",
            new_name="TagCloth",
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-13 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="postbook",
            options={
                "verbose_name": "добавить книгу",
                "verbose_name_plural": "список книг",
            },
        ),
        migrations.AlterField(
            model_name="postbook",
            name="pages",
            field=models.PositiveIntegerField(verbose_name="Сколько страниц"),
        ),
        migrations.AlterField(
            model_name="postbook",
            name="video",
            field=models.URLField(blank=True, verbose_name="Укажите ссылку на видео"),
        ),
    ]

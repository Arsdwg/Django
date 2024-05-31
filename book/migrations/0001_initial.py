# Generated by Django 5.0.4 on 2024-05-10 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PostBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Наззвание")),
                ("author", models.CharField(max_length=100, verbose_name="Автор")),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="images/", verbose_name="Укажите фото"
                    ),
                ),
                ("descript", models.TextField(verbose_name="Описание")),
                (
                    "music",
                    models.FileField(
                        blank=True, upload_to="audio/", verbose_name="Аудио озвучка"
                    ),
                ),
                ("video", models.URLField(verbose_name="Укажите ссылку на видео")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("драма", "драма"),
                            ("комедия", "комедия"),
                            ("хоррор", "хоррор"),
                            ("сказка", "сказка"),
                        ],
                        max_length=100,
                        verbose_name="Категория",
                    ),
                ),
                ("review", models.TextField(verbose_name="Отзыв специалиста")),
                ("pages", models.TextField(verbose_name="Сколько страниц")),
                (
                    "time_book",
                    models.PositiveIntegerField(verbose_name="укажите время новости"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

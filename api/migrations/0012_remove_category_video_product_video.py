# Generated by Django 4.2.2 on 2023-09-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_alter_productoptionitem_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="video",
        ),
        migrations.AddField(
            model_name="product",
            name="video",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="categories/video/",
                verbose_name="Видео",
            ),
        ),
    ]

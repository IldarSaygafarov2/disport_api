# Generated by Django 4.2.2 on 2023-11-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_product_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video_name',
            field=models.CharField(blank=True, default='.mp4', help_text="Нужно написать название видео до точки. Пример: 'test_video.mp4' ", max_length=300, verbose_name='Название видео'),
        ),
    ]
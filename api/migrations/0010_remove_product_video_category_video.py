# Generated by Django 4.2.2 on 2023-08-27 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_product_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='video',
        ),
        migrations.AddField(
            model_name='category',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='categories/video/', verbose_name='Видео'),
        ),
    ]

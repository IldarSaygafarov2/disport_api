# Generated by Django 4.2.2 on 2023-08-27 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_product_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='products/video/', verbose_name='Видео'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-11-26 15:15

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_product_video_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='preview', verbose_name='Заставка'),
        ),
    ]

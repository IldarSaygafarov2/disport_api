# Generated by Django 4.2.2 on 2023-08-10 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_categorycharacteristics_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorycharacteristicsoptions',
            name='category_characteristics',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='api.categorycharacteristics'),
        ),
    ]

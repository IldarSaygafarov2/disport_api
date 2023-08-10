# Generated by Django 4.2.2 on 2023-08-10 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_productcharacteristicstitle_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryCharacteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='characteristics', to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryCharacteristicsOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=150)),
                ('category_characteristics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categorycharacteristics')),
            ],
        ),
    ]

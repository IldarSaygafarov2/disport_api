# Generated by Django 4.2.2 on 2023-08-26 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_product_vendor_code"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["pk"],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AlterField(
            model_name="productoptionitem",
            name="name",
            field=models.TextField(
                max_length=155, verbose_name="Дополнительная характеристика"
            ),
        ),
    ]
# Generated by Django 4.2.2 on 2023-08-13 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_testmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcharacteristics',
            name='product',
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
        migrations.DeleteModel(
            name='ProductCharacteristics',
        ),
    ]

# Generated by Django 4.1 on 2022-11-08 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_remove_productphoto_product_product_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productphoto',
            name='position',
        ),
        migrations.AddField(
            model_name='productphoto',
            name='description',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
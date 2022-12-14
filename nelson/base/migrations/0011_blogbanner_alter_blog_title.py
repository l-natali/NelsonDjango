# Generated by Django 4.1 on 2022-10-18 18:18

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_blog_alter_writeus_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('photo', models.ImageField(upload_to=base.models.About.get_file_name)),
            ],
        ),
    ]

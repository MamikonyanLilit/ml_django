# Generated by Django 4.2.7 on 2023-11-08 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_gallery_img_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='img_open',
            field=models.ImageField(upload_to='media', verbose_name='Drop down image'),
        ),
    ]

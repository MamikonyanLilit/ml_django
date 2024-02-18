# Generated by Django 4.2.7 on 2023-11-08 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='Image')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('text', models.CharField(max_length=120, verbose_name='text')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
        ),
    ]

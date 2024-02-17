# Generated by Django 4.2.6 on 2023-11-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='img')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('text1', models.TextField(verbose_name='text1')),
                ('text2', models.TextField(verbose_name='text2')),
            ],
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_contact_email_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='email'),
        ),
    ]

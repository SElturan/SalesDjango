# Generated by Django 3.2 on 2023-06-24 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codegenerate',
            name='regular_customer',
        ),
        migrations.AddField(
            model_name='user',
            name='regular_customer',
            field=models.BooleanField(default=False, verbose_name='Постоянный клиент'),
        ),
    ]

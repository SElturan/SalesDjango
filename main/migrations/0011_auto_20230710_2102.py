# Generated by Django 3.2 on 2023-07-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_user_age_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regularuser',
            name='summ',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Сумма товара'),
        ),
        migrations.AlterField(
            model_name='regularuser',
            name='visits',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Посещение'),
        ),
    ]

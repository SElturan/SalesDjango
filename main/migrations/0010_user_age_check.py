# Generated by Django 3.2 on 2023-07-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_user_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age_check',
            field=models.BooleanField(default=False, verbose_name='Возраст подтвержден'),
        ),
    ]
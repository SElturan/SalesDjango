# Generated by Django 3.2 on 2023-06-27 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20230626_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codegenerate',
            name='purchase_privileges',
        ),
        migrations.RemoveField(
            model_name='user',
            name='regular_customer',
        ),
        migrations.CreateModel(
            name='RegularUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summ', models.IntegerField(blank=True, null=True, verbose_name='Сумма товара')),
                ('visits', models.IntegerField(verbose_name='Посещение')),
                ('discount', models.IntegerField(default=3, verbose_name='Процент скидки')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Постоянный клиент',
                'verbose_name_plural': 'Постоянные клиенты',
            },
        ),
    ]

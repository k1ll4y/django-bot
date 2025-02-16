# Generated by Django 5.0.3 on 2024-03-27 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_offer_requirement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Является ли администратором'),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(null=True, verbose_name='юзернейм пользователя'),
        ),
    ]

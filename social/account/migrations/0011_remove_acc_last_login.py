# Generated by Django 5.0.1 on 2024-01-23 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_acc_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acc',
            name='last_login',
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_acc_usr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acc',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]

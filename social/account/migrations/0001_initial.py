# Generated by Django 5.0.1 on 2024-01-19 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='acc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
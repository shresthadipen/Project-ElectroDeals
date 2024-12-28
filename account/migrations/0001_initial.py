# Generated by Django 5.1.3 on 2024-12-27 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signup_username', models.CharField(max_length=100)),
                ('signup_email', models.EmailField(max_length=254)),
                ('signup_password', models.CharField(max_length=20)),
            ],
        ),
    ]
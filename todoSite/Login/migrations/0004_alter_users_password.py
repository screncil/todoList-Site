# Generated by Django 5.0.2 on 2024-02-22 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_alter_users_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-25 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_alter_list_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='id',
            new_name='_id',
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-25 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_rename_id_list__id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='_id',
            new_name='id',
        ),
    ]

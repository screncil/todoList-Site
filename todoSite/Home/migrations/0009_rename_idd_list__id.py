# Generated by Django 5.0.2 on 2024-02-25 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_list_idd_alter_list_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='idd',
            new_name='_id',
        ),
    ]
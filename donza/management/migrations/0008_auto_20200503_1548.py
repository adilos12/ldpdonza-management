# Generated by Django 3.0.5 on 2020-05-03 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_auto_20200503_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ploeglid',
            old_name='lid_id',
            new_name='lid',
        ),
        migrations.RenameField(
            model_name='ploeglid',
            old_name='ploeg_id',
            new_name='ploeg',
        ),
    ]

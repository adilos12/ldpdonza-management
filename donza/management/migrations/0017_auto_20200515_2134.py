# Generated by Django 3.0.5 on 2020-05-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0016_auto_20200515_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betaling',
            name='afgelost_bedrag',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='betaling',
            name='origineel_bedrag',
            field=models.FloatField(),
        ),
    ]

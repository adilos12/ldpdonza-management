# Generated by Django 3.0.5 on 2020-05-13 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_auto_20200511_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ploeg',
            name='geslacht',
            field=models.CharField(choices=[('m', 'Man'), ('v', 'Vrouw'), ('g', 'Gemengd')], default='m', max_length=2),
        ),
        migrations.CreateModel(
            name='Betaling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origineel_bedrag', models.DecimalField(decimal_places=2, max_digits=4)),
                ('afgelost_bedrag', models.DecimalField(decimal_places=2, max_digits=4)),
                ('mails_verstuurd', models.CharField(max_length=500)),
                ('mededeling', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Lid')),
                ('seizoen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Seizoen')),
            ],
        ),
    ]
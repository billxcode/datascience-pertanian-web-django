# Generated by Django 2.1.3 on 2018-11-12 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MOORA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kriteria',
            name='periode',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

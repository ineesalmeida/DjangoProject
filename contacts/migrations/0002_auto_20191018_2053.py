# Generated by Django 2.2.6 on 2019-10-18 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 10, 18, 20, 53, 43, 905661)),
        ),
    ]

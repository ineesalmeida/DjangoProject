# Generated by Django 2.2.6 on 2019-10-16 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20191016_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2),
        ),
    ]
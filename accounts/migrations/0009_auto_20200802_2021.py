# Generated by Django 3.0.8 on 2020-08-02 14:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='description',
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 2, 14, 51, 34, 174390, tzinfo=utc)),
        ),
    ]

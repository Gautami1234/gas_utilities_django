# Generated by Django 5.1.6 on 2025-02-19 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportticket',
            name='service_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requests.servicerequest'),
        ),
    ]

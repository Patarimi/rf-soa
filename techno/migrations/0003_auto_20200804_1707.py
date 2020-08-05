# Generated by Django 3.0.6 on 2020-08-04 15:07

import django.contrib.postgres.fields.hstore
from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techno', '0002_components_type_perf_list'),
    ]

    operations = [
        HStoreExtension(),
        migrations.RemoveField(
            model_name='component',
            name='comp_type',
        ),
        migrations.AddField(
            model_name='component',
            name='comp_type_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='techno.Components_Type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='component',
            name='key_perf',
            field=django.contrib.postgres.fields.hstore.HStoreField(default=""),
            preserve_default=False,
        ),
    ]

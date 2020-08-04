# Generated by Django 3.0.3 on 2020-08-04 09:12

from django.db import migrations, models
import techno.models


class Migration(migrations.Migration):

    dependencies = [
        ('techno', '0002_components_type_perf_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='comp_type',
        ),
        migrations.AddField(
            model_name='component',
            name='comp_type_id',
            field=models.IntegerField(default='2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='component',
            name='key_perf',
            field=techno.models.KeyPerfField(default="{'area': 5.0, 'fc': 10000000000.0}"),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-31 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techno', '0008_auto_20201231_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='component',
            old_name='comp_type_id',
            new_name='comp_type',
        ),
    ]

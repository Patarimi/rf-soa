# Generated by Django 3.1.4 on 2020-12-28 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techno', '0003_auto_20200804_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Key_Param',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('units', models.CharField(blank=True, choices=[('Hz', 'Hz'), ('W', 'W'), ('%', '%')], max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='component',
            name='key_perf',
        ),
        migrations.RemoveField(
            model_name='components_type',
            name='perf_list',
        ),
        migrations.RemoveField(
            model_name='key_perf',
            name='name',
        ),
        migrations.AddField(
            model_name='key_perf',
            name='component',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='techno.component'),
        ),
        migrations.AddField(
            model_name='key_perf',
            name='value',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='component',
            name='perf_record',
            field=models.ManyToManyField(through='techno.Key_Perf', to='techno.Key_Param'),
        ),
        migrations.AddField(
            model_name='key_perf',
            name='key_param',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='techno.key_param'),
        ),
    ]

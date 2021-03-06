# Generated by Django 3.0.6 on 2020-07-30 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key_Perf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Techno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('provider', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='techno.Provider')),
            ],
        ),
        migrations.CreateModel(
            name='Components_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doi', models.URLField()),
                ('comp_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techno.Components_Type')),
                ('techno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techno.Techno')),
            ],
        ),
    ]

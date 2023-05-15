# Generated by Django 4.2.1 on 2023-05-12 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bjj_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('contact_phone', models.CharField(max_length=20)),
                ('information', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('weekday', models.CharField(choices=[('monday', 'Понеділок'), ('tuesday', 'Вівторок'), ('wednesday', 'Середа'), ('thursday', 'Четвер'), ('friday', "П'ятниця"), ('saturday', 'Субота'), ('sunday', 'Неділя')], max_length=9)),
                ('forma', models.CharField(max_length=20)),
                ('group', models.CharField(max_length=255)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bjj_app.trainer', verbose_name='Тренер')),
            ],
            options={
                'verbose_name': 'Schedule',
                'verbose_name_plural': 'Schedule',
            },
        ),
    ]

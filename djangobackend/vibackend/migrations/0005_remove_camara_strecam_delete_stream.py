# Generated by Django 4.0.2 on 2022-03-03 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vibackend', '0004_stream_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camara',
            name='streCam',
        ),
        migrations.DeleteModel(
            name='Stream',
        ),
    ]
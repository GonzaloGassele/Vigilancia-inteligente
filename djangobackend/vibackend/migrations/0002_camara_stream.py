# Generated by Django 4.0.2 on 2022-03-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vibackend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='camara',
            name='stream',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
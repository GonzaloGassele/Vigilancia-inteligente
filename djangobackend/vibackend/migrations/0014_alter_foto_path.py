# Generated by Django 4.0.2 on 2022-03-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vibackend', '0013_alter_foto_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='path',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
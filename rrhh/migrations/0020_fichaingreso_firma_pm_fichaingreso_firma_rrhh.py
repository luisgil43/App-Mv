# Generated by Django 5.2.1 on 2025-06-20 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0019_remove_fichaingreso_afp_remove_fichaingreso_banco_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichaingreso',
            name='firma_pm',
            field=models.ImageField(blank=True, null=True, upload_to='firmas/'),
        ),
        migrations.AddField(
            model_name='fichaingreso',
            name='firma_rrhh',
            field=models.ImageField(blank=True, null=True, upload_to='firmas/'),
        ),
    ]

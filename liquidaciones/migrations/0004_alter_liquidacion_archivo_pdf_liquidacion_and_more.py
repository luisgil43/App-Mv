# Generated by Django 5.2.1 on 2025-05-23 02:59

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liquidaciones', '0003_liquidacion_archivo_pdf_liquidacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquidacion',
            name='archivo_pdf_liquidacion',
            field=models.FileField(blank=True, null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='pdf_originales/', verbose_name='Liquidación de sueldo'),
        ),
        migrations.AlterField(
            model_name='liquidacion',
            name='pdf_firmado',
            field=models.FileField(blank=True, null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='pdf_firmados/', verbose_name='Liquidación de sueldo firmada'),
        ),
    ]

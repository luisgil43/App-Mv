# Generated by Django 5.2.1 on 2025-05-21 01:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tecnicos', '0004_tecnico_firma_digital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liquidacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=20)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('archivo_pdf', models.FileField(upload_to='liquidaciones/')),
                ('firmada', models.BooleanField(default=False)),
                ('fecha_firma', models.DateTimeField(blank=True, null=True)),
                ('pdf_firmado', models.FileField(blank=True, null=True, upload_to='liquidaciones_firmadas/')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tecnicos.tecnico')),
            ],
        ),
    ]

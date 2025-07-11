# Generated by Django 5.2.1 on 2025-06-17 01:04

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0008_diasvacacionestomadosmanualmente'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudvacaciones',
            name='aprobado_por_pm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vacaciones_aprobadas_pm', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solicitudvacaciones',
            name='aprobado_por_rrhh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vacaciones_aprobadas_rrhh', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solicitudvacaciones',
            name='aprobado_por_supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vacaciones_aprobadas_supervisor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='solicitudvacaciones',
            name='dias_solicitados',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='solicitudvacaciones',
            name='estatus',
            field=models.CharField(default='pendiente_supervisor', max_length=30),
        ),
        migrations.AlterField(
            model_name='solicitudvacaciones',
            name='fecha_solicitud',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='solicitudvacaciones',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_vacaciones', to=settings.AUTH_USER_MODEL),
        ),
    ]

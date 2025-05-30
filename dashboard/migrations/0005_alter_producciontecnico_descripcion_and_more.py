# Generated by Django 5.2.1 on 2025-05-22 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_producciontecnico_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producciontecnico',
            name='descripcion',
            field=models.TextField(blank=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='producciontecnico',
            name='fecha_aprobacion',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Aprobación'),
        ),
        migrations.AlterField(
            model_name='producciontecnico',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='ID de Producción'),
        ),
        migrations.AlterField(
            model_name='producciontecnico',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto'),
        ),
        migrations.AlterField(
            model_name='producciontecnico',
            name='status',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado')], max_length=20, verbose_name='Estado'),
        ),
    ]

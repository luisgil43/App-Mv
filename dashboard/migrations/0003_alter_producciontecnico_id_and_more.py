# Generated by Django 5.2.1 on 2025-05-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_producciontecnico_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producciontecnico',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID Manual'),
        ),
        migrations.AlterField(
            model_name='producciontecnico',
            name='monto',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]

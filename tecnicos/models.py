from django.db import models
from django.contrib.auth.models import User
# Importar el storage de Cloudinary para usarlo explícitamente en el campo
from cloudinary_storage.storage import MediaCloudinaryStorage


class Tecnico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firma_digital = models.ImageField(
        upload_to='firmas/',
        blank=True,
        null=True,
        # Agregamos storage para asegurarnos que use Cloudinary,
        # esto puede evitar problemas si el DEFAULT_FILE_STORAGE no está funcionando bien.
        storage=MediaCloudinaryStorage()
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Produccion(models.Model):
    ESTADOS = [
        ('cancelado', 'Cancelado'),
        ('pendiente', 'Pendiente'),
        ('en_ejecucion', 'En ejecución'),
        ('finalizado', 'Finalizado'),
    ]

    tecnico = models.ForeignKey(
        Tecnico, on_delete=models.CASCADE, related_name='producciones')
    supervisor = models.ForeignKey(
        Supervisor, on_delete=models.SET_NULL, null=True, blank=True, related_name='producciones')
    fecha_aprobacion = models.DateField(null=True, blank=True)
    estado = models.CharField(
        max_length=20, choices=ESTADOS, default='pendiente')
    total_pago = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Producción {self.id} - Técnico: {self.tecnico} - Estado: {self.estado}"


class Curso(models.Model):
    tecnico = models.ForeignKey(
        Tecnico, on_delete=models.CASCADE, related_name='cursos')
    nombre_curso = models.CharField(max_length=255)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_curso} - {self.tecnico}"

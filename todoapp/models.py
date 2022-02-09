from django.db.models.signals import post_delete
from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from TestNewsan.constant import FORMATOS_ARCHIVOS_PERMITIDOS
from TestNewsan.settings import MEDIA_ROOT


class Todo(models.Model):

    def formatos_soportados():
        formatos = "("
        cantidad_formatos = len(FORMATOS_ARCHIVOS_PERMITIDOS)
        for pos_formato in range(cantidad_formatos - 1):
            formatos += FORMATOS_ARCHIVOS_PERMITIDOS[pos_formato] + ", "
        formatos += FORMATOS_ARCHIVOS_PERMITIDOS[cantidad_formatos - 1] + ")"
        return formatos

    class ValorEstado(models.TextChoices):
        PENDIENTE = "P", "Pendiente"
        RESUELTO = "R", "Resuelto"

    descripcion = models.CharField(max_length=64)
    estado = models.CharField(
        max_length=1, choices=ValorEstado.choices, default=ValorEstado.PENDIENTE)
    adjunto = models.FileField(blank=True, null=True ,upload_to=MEDIA_ROOT,validators=[FileExtensionValidator(
        allowed_extensions=FORMATOS_ARCHIVOS_PERMITIDOS, message="Formatos soportados " + formatos_soportados())])

    def get_absolute_url(self):
        return reverse("listar-todo")
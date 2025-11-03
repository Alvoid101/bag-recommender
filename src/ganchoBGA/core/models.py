from django.db import models

# Create your models here.

class Bolso(models.Model):
    """
    Modelo para representar los bolsos del catálogo.
    """
    product_display_name = models.CharField(
        max_length=255,
        verbose_name="Nombre del Producto",
        help_text="Nombre descriptivo del bolso"
    )
    base_colour = models.CharField(
        max_length=50,
        verbose_name="Color Base",
        help_text="Color principal del bolso"
    )
    image = models.URLField(
        max_length=500,
        verbose_name="URL de Imagen",
        help_text="URL de la imagen del producto",
        blank=True,
        null=True
    )
    local_image = models.ImageField(
        upload_to='bolsos/',
        verbose_name="Imagen Local",
        help_text="Imagen del bolso",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creación"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Fecha de Actualización"
    )

    class Meta:
        verbose_name = "Bolso"
        verbose_name_plural = "Bolsos"
        ordering = ['product_display_name']

    def __str__(self):
        return f"{self.product_display_name} - {self.base_colour}"

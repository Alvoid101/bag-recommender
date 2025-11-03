from django.contrib import admin
from .models import Bolso

# Register your models here.

@admin.register(Bolso)
class BolsoAdmin(admin.ModelAdmin):
    list_display = ('product_display_name', 'base_colour', 'created_at')
    list_filter = ('base_colour', 'created_at')
    search_fields = ('product_display_name', 'base_colour')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Información del Producto', {
            'fields': ('product_display_name', 'base_colour')
        }),
        ('Imágenes', {
            'fields': ('image', 'local_image')
        }),
        ('Metadatos', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

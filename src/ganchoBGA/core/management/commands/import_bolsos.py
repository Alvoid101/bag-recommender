import csv
import os
from django.core.management.base import BaseCommand
from core.models import Bolso


class Command(BaseCommand):
    help = 'Importa los bolsos desde el archivo CSV filtered_bags_database.csv'

    def handle(self, *args, **options):
        # Ruta al archivo CSV
        csv_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))),
            'CSV',
            'filtered_bags_database.csv'
        )
        
        if not os.path.exists(csv_path):
            self.stdout.write(
                self.style.ERROR(f'No se encontró el archivo: {csv_path}')
            )
            return
        
        self.stdout.write(
            self.style.SUCCESS(f'Leyendo archivo: {csv_path}')
        )
        
        # Contador de registros
        created_count = 0
        updated_count = 0
        error_count = 0
        
        # Limpiar la tabla antes de importar (opcional)
        # Bolso.objects.all().delete()
        # self.stdout.write(self.style.WARNING('Tabla Bolso limpiada'))
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row_num, row in enumerate(reader, start=2):  # start=2 porque la fila 1 es el header
                    try:
                        # Extraer datos del CSV
                        product_name = row.get('productDisplayName', '').strip()
                        base_colour = row.get('baseColour', '').strip()
                        image_url = row.get('image', '').strip()
                        local_image = row.get('local_image', '').strip()
                        
                        # Validar que al menos tengamos nombre y color
                        if not product_name or not base_colour:
                            self.stdout.write(
                                self.style.WARNING(
                                    f'Fila {row_num}: Faltan datos obligatorios (nombre o color)'
                                )
                            )
                            error_count += 1
                            continue
                        
                        # Crear o actualizar el bolso
                        bolso, created = Bolso.objects.update_or_create(
                            product_display_name=product_name,
                            base_colour=base_colour,
                            defaults={
                                'image': image_url if image_url else None,
                                'local_image': local_image if local_image else None,
                            }
                        )
                        
                        if created:
                            created_count += 1
                        else:
                            updated_count += 1
                        
                        # Mostrar progreso cada 100 registros
                        if (created_count + updated_count) % 100 == 0:
                            self.stdout.write(
                                self.style.SUCCESS(
                                    f'Procesados: {created_count + updated_count} bolsos'
                                )
                            )
                    
                    except Exception as e:
                        error_count += 1
                        self.stdout.write(
                            self.style.ERROR(
                                f'Error en fila {row_num}: {str(e)}'
                            )
                        )
            
            # Resumen final
            self.stdout.write(
                self.style.SUCCESS('\n' + '='*50)
            )
            self.stdout.write(
                self.style.SUCCESS('IMPORTACIÓN COMPLETADA')
            )
            self.stdout.write(
                self.style.SUCCESS('='*50)
            )
            self.stdout.write(
                self.style.SUCCESS(f'✓ Registros creados: {created_count}')
            )
            self.stdout.write(
                self.style.SUCCESS(f'✓ Registros actualizados: {updated_count}')
            )
            if error_count > 0:
                self.stdout.write(
                    self.style.WARNING(f'⚠ Errores: {error_count}')
                )
            self.stdout.write(
                self.style.SUCCESS(f'✓ Total procesados: {created_count + updated_count}')
            )
            self.stdout.write(
                self.style.SUCCESS('='*50 + '\n')
            )
        
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f'No se pudo abrir el archivo: {csv_path}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error general: {str(e)}')
            )

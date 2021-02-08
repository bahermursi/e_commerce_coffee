from django.db import models

PRODUCT_TYPE_CHOICES = (
    ("COFFEE_MACHINE_LARGE", "COFFEE_MACHINE_LARGE"),
    ("COFFEE_MACHINE_SMALL","COFFEE_MACHINE_SMALL"),
    ("ESPRESSO_MACHINE","ESPRESSO_MACHINE"),
 )

class Machine(models.Model):
    product_type = models.CharField(
        max_length = 100, 
        choices = PRODUCT_TYPE_CHOICES, 
        default = 'COFFEE_MACHINE_LARGE',
        blank=True
    ) 
    description = models.TextField(max_length=254, default="")
    water_line_compatible = models.BooleanField(default=False)
    code = models.TextField(max_length=254, default="")
    
    class meta:
        verbose_name        = 'Machine'
        verbose_name_plural = 'Machines'
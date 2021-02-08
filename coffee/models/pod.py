from django.db import models


PRODUCT_TYPE_CHOICES = (
    ("COFFEE_POD_LARGE", "COFFEE_POD_LARGE"),
    ("COFFEE_POD_SMALL","COFFEE_POD_SMALL"),
    ("ESPRESSO_POD","ESPRESSO_POD"),
)

COFFE_FLAVOR_CHOICES = (
    ("COFFEE_FLAVOR_VANILLA", "COFFEE_FLAVOR_VANILLA"),
    ("COFFEE_FLAVOR_CARAMEL","COFFEE_FLAVOR_CARAMEL"),
    ("COFFEE_FLAVOR_PSL","COFFEE_FLAVOR_PSL"),
    ("COFFEE_FLAVOR_MOCHA","COFFEE_FLAVOR_MOCHA"),
    ("COFFEE_FLAVOR_HAZELNUT","COFFEE_FLAVOR_HAZELNUT"),
)

PACK_SIZE_CHOICES = (
    ("1_dozen", "1_dozen"),
    ("3 dozen ", "3 dozen "),
    ("5_dozen", "5_dozen"),
    ("7_dozen", "7_dozen"),
)


class Pod(models.Model):
    product_type = models.CharField(
        max_length = 100, 
        choices = PRODUCT_TYPE_CHOICES, 
        default = 'COFFEE_POD_LARGE',
        blank=True
    ) 
    coffee_flavor = models.CharField(
        max_length = 100, 
        choices = COFFE_FLAVOR_CHOICES, 
        default = 'COFFEE_FLAVOR_VANILLA',
        blank=True
    )
    pack_size = models.CharField(
        max_length = 100, 
        choices = PACK_SIZE_CHOICES, 
        default = '1_dozen',
        blank=True
    )
    description = models.TextField(max_length=254, default="")
    code = models.TextField(max_length=254, default="")
    
    class meta:
        verbose_name        = 'Pod'
        verbose_name_plural = 'Pods'
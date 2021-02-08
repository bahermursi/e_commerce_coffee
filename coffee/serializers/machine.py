"""
Coffee Machines model and validation serializers. 
"""

from coffee.models.machine import Machine
from rest_framework import serializers

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        exclude = ['id']


class MachineValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('product_type','water_line_compatible')

from coffee.models.machine import Machine
from rest_framework import serializers
from icecream import ic

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        # fields = '__all__'
        exclude = ['id']


class MachineValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('product_type','water_line_compatible')

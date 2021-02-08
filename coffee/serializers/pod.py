from coffee.models.pod import Pod
from rest_framework import serializers
from icecream import ic

class PodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pod
        exclude = ['id']


class PodValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pod
        fields = ('product_type','coffee_flavor','pack_size')

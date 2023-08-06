from rest_framework import serializers
from .models import pathogenics

class pathogenicSerializers(serializers.ModelSerializer):
    class Meta:
        model = pathogenics
        fields = '__all__'
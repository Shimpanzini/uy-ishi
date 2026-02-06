from rest_framework import serializers
from .models import Maktab, Oquvchi, Oqituvchi, Gurux


class MaktabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maktab
        fields = '__all__'


class OquvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oquvchi
        fields = '__all__'


class OqituvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oqituvchi
        fields = '__all__'


class GuruxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gurux
        fields = '__all__'

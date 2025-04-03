from rest_framework import serializers
from .models import Eyewear

class EyewearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eyewear
        fields = '__all__'

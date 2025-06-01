from rest_framework import serializers
from .models import TemplateComponent

class TemplateComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateComponent
        fields = '__all__'

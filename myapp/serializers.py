from rest_framework import serializers
from .models import Users

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['FullName', 'CardNumber', 'inventory']
        
        extra_kwargs = {
            'CardNumber': {'write_only': True}
        }

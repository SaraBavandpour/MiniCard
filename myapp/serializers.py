from rest_framework import serializers
from .models import Users

class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['FullName', 'CardNumber', 'inventory']
        
        
class ReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['CardNumber', 'amount']
        
class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['inventory']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


        

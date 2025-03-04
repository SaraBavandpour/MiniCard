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
        
        

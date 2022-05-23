from rest_framework import serializers
from .models import Review, ClientVideo


class ClientVideoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = ClientVideo
        fields = '__all__'
        
        
class ReviewSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
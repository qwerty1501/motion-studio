from rest_framework import serializers
from .models import FeedbackLink, OurClient


class FeedbackLinkSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = FeedbackLink
        fields = '__all__'
        
        
class OurClientSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = OurClient
        fields = '__all__'
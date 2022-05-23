from rest_framework import serializers
from .models import Order, CreateStaff, Vacancy, Feedback


class OrderSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'
        
        
class CreateStaffSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = CreateStaff
        fields = '__all__'
        
        
class VacancySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Vacancy
        fields = '__all__'
        
        
class FeedbackSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Feedback
        fields = '__all__'

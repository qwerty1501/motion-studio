from django.shortcuts import render
from rest_framework import generics

from .serializers import OrderSerializers, CreateStaffSerializers, VacancySerializers, FeedbackSerializers
from .models import Order, CreateStaff, Vacancy, Feedback


class OrderCreateListView(generics.ListCreateAPIView):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()
    
    
class OrderDeleteView(generics.DestroyAPIView):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()
    

class CreateStaffCreateListView(generics.ListCreateAPIView):
    serializer_class = CreateStaffSerializers
    queryset = CreateStaff.objects.all()
    
    
class CreateSteffDeleteView(generics.DestroyAPIView):
    serializer_class = CreateStaffSerializers
    queryset = CreateStaff.objects.all()
    
    
class VacancyCreateListView(generics.ListCreateAPIView):
    serializer_class = VacancySerializers
    queryset = Vacancy.objects.all()


class VacancyDeleteView(generics.DestroyAPIView):
    serializer_class = VacancySerializers
    queryset = Vacancy.objects.all()
    
    
class FeedbackCreateListView(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializers
    queryset = Feedback.objects.all()
    
    
class FeedbackDeleteView(generics.DestroyAPIView):
    serializer_class = FeedbackSerializers()
    queryset = Feedback.objects.all()
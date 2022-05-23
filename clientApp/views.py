from django.shortcuts import render
from rest_framework import generics

from .serializers import ReviewSerializers, ClientVideoSerializers
from .models import Review, ClientVideo


class ReviewCreateListView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializers
    queryset = Review.objects.all()
    
    
class ReviewDeleteView(generics.DestroyAPIView):
    serializer_class = ReviewSerializers
    queryset = Review.objects.all()
    
    
class ClientVideoCreateListView(generics.ListCreateAPIView):
    serializer_class = ClientVideoSerializers
    queryset = ClientVideo.objects.all()
    
    
class ClientVideoDeleteView(generics.DestroyAPIView):
    serializer_class = ClientVideoSerializers
    queryset = ClientVideo.objects.all()
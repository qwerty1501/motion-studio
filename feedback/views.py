from django.shortcuts import render
from rest_framework import generics

from .serializers import FeedbackLinkSerializers, OurClientSerializers
from .models import FeedbackLink, OurClient


class FeedbackLinkCreateListView(generics.ListCreateAPIView):
    serializer_class = FeedbackLinkSerializers
    queryset = FeedbackLink.objects.all()
    
    
class FeedbackLinkDeleteView(generics.DestroyAPIView):
    serializer_class = FeedbackLinkSerializers
    queryset = FeedbackLink.objects.all()
    
    
class OurClientCreateListView(generics.ListCreateAPIView):
    serializer_class = OurClientSerializers
    queryset = OurClient.objects.all()
    
    
class OurClientDeleteView(generics.DestroyAPIView):
    serializer_class = OurClientSerializers
    queryset = OurClient.objects.all()
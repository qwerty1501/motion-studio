from django.urls import path
from .views import FeedbackLinkCreateListView, FeedbackLinkDeleteView, OurClientCreateListView, OurClientDeleteView


urlpatterns = [
    path('feedback/link/', FeedbackLinkCreateListView.as_view()),
    path('feedback/link/delete/<int:pk>/', FeedbackLinkDeleteView.as_view()),
    path('ourclient/link/', OurClientCreateListView.as_view()),
    path('ourclient/link/delete/<int:pk>/', OurClientDeleteView.as_view()),
]
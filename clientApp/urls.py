from django.urls import path
from .views import ReviewCreateListView, ReviewDeleteView, ClientVideoCreateListView, ClientVideoDeleteView


urlpatterns = [
    path('review/', ReviewCreateListView.as_view()),
    path('review/delete/<int:pk>/', ReviewDeleteView.as_view()),
    path('clientvideo/', ClientVideoCreateListView.as_view()),
    path('clientvideo/delete/<int:pk>/', ClientVideoDeleteView.as_view()),
]
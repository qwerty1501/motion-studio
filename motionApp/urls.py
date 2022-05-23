from django.urls import path
from .views import OrderCreateListView, CreateStaffCreateListView, VacancyCreateListView, FeedbackCreateListView
from .views import OrderDeleteView, CreateSteffDeleteView, VacancyDeleteView, FeedbackDeleteView

urlpatterns = [
    path('project/', OrderCreateListView.as_view()),
    path('staff/', CreateStaffCreateListView.as_view()),
    path('vacancy/', VacancyCreateListView.as_view()),
    path('feedback/', FeedbackCreateListView.as_view()),
    # Delete
    path('projects/delete/<int:pk>/', OrderDeleteView.as_view()),
    path('staff/delete/<int:pk>/', CreateSteffDeleteView.as_view()),
    path('vacancy/delete/<int:pk>/', VacancyDeleteView.as_view()),
    path('feedback/delete/<int:pk>/', FeedbackDeleteView.as_view()),
]
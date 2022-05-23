from django.contrib import admin
from .models import Order, CreateStaff, Vacancy, Feedback


admin.site.register(Order)
admin.site.register(CreateStaff)
admin.site.register(Vacancy)
admin.site.register(Feedback)
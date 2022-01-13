from .views import StudentList, StudentDetail
from django.urls import path

urlpatterns = [
    path('api/students/', StudentList.as_view()), 
    path('api/students/<int:pk>/', StudentDetail.as_view()),
]
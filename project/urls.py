from django.urls import path
from .views import ProjectDetail

urlpatterns = [
    path('index', ProjectDetail.as_view()),
]
from django.urls import path
from .views import ProjectDetail, ProjectAllList

urlpatterns = [
    path('index', ProjectDetail.as_view()),
    path('all', ProjectAllList.as_view()),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('project/<int:pk>', ProjectDetailView.as_view(), name="project_details"),
]
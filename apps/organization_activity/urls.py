from django.urls import path, include
from .views import *

urlpatterns = [
    path('project/', include([
        path('', ProjectDetailView.as_view(), name="project_list"),
        path('<int:pk>', ProjectDetailView.as_view(), name="project_details"),
    ]))
]

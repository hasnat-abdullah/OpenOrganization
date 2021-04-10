from django.urls import path
from apps.organization_details.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('contact', ContactView.as_view(), name="contact")
]
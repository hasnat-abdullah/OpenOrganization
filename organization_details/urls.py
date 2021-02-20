from django.urls import path, include
from organization_details.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index" )
]
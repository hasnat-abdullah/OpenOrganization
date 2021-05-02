from django.urls import path, include
from apps.organization_details.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('contact', ContactView.as_view(), name="contact"),
    path('subscriber/add/', SubscriptionView.as_view(), name="subscriber_add"),
    path('notices/',include([
            path('',NoticeListView.as_view(), name="notice_list"),
            path('<int:pk>', NoticeDetailView.as_view(), name="notice_details"),
        ])),
]
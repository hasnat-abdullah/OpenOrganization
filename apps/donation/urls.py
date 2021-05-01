from django.urls import path, include
from .views import DonationRecordListView, DonationDetailView, DonateView

urlpatterns = [
    path('records/',include([
        path('',DonationRecordListView.as_view(), name="donation_list"),
        path('<int:pk>', DonationDetailView.as_view(), name="donation_details"),
    ])),
    path('donate', DonateView.as_view(), name="donate"),
]
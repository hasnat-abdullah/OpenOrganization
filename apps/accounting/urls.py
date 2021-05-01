from django.urls import path, include
from .views import DebitRecordListView, DebitDetailView

urlpatterns = [
    path('debit/',include([
        path('',DebitRecordListView.as_view(), name="expense_list"),
        path('<int:pk>', DebitDetailView.as_view(), name="expense_details"),
    ]))
]
from django.urls import path
from logs.views import LogView

urlpatterns = [
    path('xfsyh25gff98gk/<str:date_n_type>', LogView.as_view(), name='log_view'),
]
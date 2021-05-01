from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.query_utils import Q
from .models import DonationRecord
from django.views import View
from logs.log import *


class DonationRecordListView(ListView):
    """List view with debit & pagination"""
    model = DonationRecord
    template_name = 'donation-record.html'
    context_object_name = 'donations'
    fields = ('donor','donated_in_project','amount','donation_details','status','created_at')
    ordering = '-id'
    paginate_by = 20

    def get_queryset(self):
        return DonationRecord.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(DonationRecordListView, self).get_context_data(**kwargs)
        debit_records = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(debit_records, self.paginate_by)
        try:
            debit_records = paginator.page(page)
        except PageNotAnInteger:
            debit_records = paginator.page(1)
        except EmptyPage:
            debit_records = paginator.page(paginator.num_pages)
        context['expenses'] = debit_records
        return context


class DonationDetailView(DetailView):
    """Debit details page view"""
    model = DonationRecord
    template_name = 'donation-record-single.html'
    context_object_name = 'donation'


class DonateView(View):
    template_name = 'charity-donation.html'

    def get(self, request):
        return render(request, self.template_name, context=None)

    def post(self, request):
        return render(request, self.template_name, context=None)
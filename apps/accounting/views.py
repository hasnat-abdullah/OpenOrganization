from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.query_utils import Q
from .models import DebitRecord
from logs.log import *


class DebitRecordListView(ListView):
    """List view with debit & pagination"""
    model = DebitRecord
    template_name = 'debit-record.html'
    context_object_name = 'expenses'
    fields = ('category','title', 'amount','debited_by','debited_to','justification','created_at')
    ordering = '-id'
    paginate_by = 20

    def get_queryset(self):
        return DebitRecord.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(DebitRecordListView, self).get_context_data(**kwargs)
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


class DebitDetailView(DetailView):
    """Debit details page view"""
    model = DebitRecord
    template_name = 'debit-record-single.html'
    context_object_name = 'expense'
